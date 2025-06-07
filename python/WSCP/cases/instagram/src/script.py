import json
import re
import os
import urllib.parse
from seleniumbase import SB
from bs4 import BeautifulSoup


def normalize_number(phone):
    return re.sub(r'\D', '', phone)

def remove_duplicate_phones(phone_numbers):
    seen = set()
    unique = []

    for phone in phone_numbers:
        normalized = normalize_number(phone)[-8:]
        if normalized not in seen:
            seen.add(normalized)
            unique.append(phone)

    return unique

def is_valid(title_text, snippet_text, only_if_exist_emails, only_if_exist_phone_numbers, emails, phone_numbers):
    if (only_if_exist_emails and len(emails) == 0) and (only_if_exist_phone_numbers and len(phone_numbers) == 0):
        return False
    
    if title_text == '':
        return False

    if 'Anúncio' not in snippet_text and \
        'Find answers ' not in snippet_text and \
        'Find help' not in snippet_text and \
        'Welcome back ' not in snippet_text and \
        'Welcome back ' not in snippet_text and \
        'nos permite' not in snippet_text and \
        'Google' not in title_text and \
        'Microsoft' not in title_text and \
        'Sign up' not in title_text and \
        'globo' not in title_text and \
        'Como entrar direto' not in title_text and \
        'LOGIN' not in title_text and \
        'YouTube' not in title_text and \
        title_text != 'Instagram' and \
        title_text != 'Yahoo' and \
        title_text != 'Outlook' and \
        title_text != 'Yahoo Mail' and \
        'Create an ' not in snippet_text:
        return True
    return False
    
def parse_number(text):
    text = text.replace(',', '').replace('.', '')
    if 'K' in text:
        return int(float(text.replace('K', '').replace(',', '').replace('.', '')) * 1000)
    elif 'M' in text:
        return int(float(text.replace('M', '').replace(',', '').replace('.', '')) * 1000000)
    else:
        return int(text)

def extract_instagram_metrics(text):
    pattern = r'([\d.,KM]+)\s+Followers,\s+([\d.,KM]+)\s+Following,\s+([\d.,KM]+)\s+Posts'
    match = re.search(pattern, text)

    if match:
        followers = parse_number(match.group(1))
        following = parse_number(match.group(2))
        posts = parse_number(match.group(3))
        return {
            "followers": followers,
            "following": following,
            "posts": posts
        }
    
    return {"followers": 0, "following": 0, "posts": 0}

def extract_phone_numbers(title_text, snippet_text):
    try:
        title_phone_numbers = re.findall(r'(?:\(?\d{2}\)?\s?)?\d{4,5}[-\s]?\d{4}', title_text)
        snippet_text_phone_numbers = re.findall(r'(?:\(?\d{2}\)?\s?)?\d{4,5}[-\s]?\d{4}', snippet_text)

        phone_numbers_1 = [ x for x in title_phone_numbers]
        phone_numbers_2 = [ x for x in snippet_text_phone_numbers]

        phone_numbers = remove_duplicate_phones(phone_numbers_1 + phone_numbers_2)
    except:
        phone_numbers = []

    return phone_numbers


def extract_emails(title_text, snippet_text):
    try:
        title_email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', title_text)
        snippet_text_email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', snippet_text)

        email_addresses_1 = [ x for x in title_email_addresses]
        email_addresses_2 = [ x for x in snippet_text_email_addresses]

        email_addresses = email_addresses_1 + email_addresses_2
    except:
        email_addresses = []

    return email_addresses


def extract_emails_from_instagram_using_duckduckgo_regex(text_to_find, pages, only_if_exist_emails=False, only_if_exist_phone_numbers=False):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    query = urllib.parse.quote_plus(f'site:instagram.com "{text_to_find}" @gmail.com @outlook.com @hotmail.com @yahoo.com @yahoo.com.br')
    base_url = f"https://duckduckgo.com/?q={query}&t=h_&ia=web"

    with SB(uc=True, headless=True) as sb:
        print("Opening browser...")
        sb.open(base_url)
        sb.sleep(3)

        for page in range(pages):
            print("Loading more results...", page + 1)
            sb.scroll_to_bottom()
            sb.sleep(2)
            if sb.is_element_visible("#more-results"):
                sb.click("#more-results")
                sb.sleep(2)
            else:
                break  

        soup = BeautifulSoup(sb.get_page_source(), "html.parser")
        article_elements = soup.find_all("article")

        results = []
        for article in article_elements:
            # article/div[3]/h2/a/span
            title_span = article.select_one("div:nth-of-type(3) h2 a span")
            # article/div[4]/div/div/span/span
            snippet_span = article.select_one("div:nth-of-type(4) div div span span")

            if title_span:
                title_text = title_span.get_text(strip=True)
                href_tag = title_span.find_parent("a")
                href = href_tag["href"] if href_tag and href_tag.has_attr("href") else ''
            else:
                title_text = ''
                href = ''

            snippet_text = snippet_span.get_text(strip=True) if snippet_span else ''

            emails = extract_emails(title_text, snippet_text)
            phone_numbers = extract_phone_numbers(title_text, snippet_text)

            if is_valid(title_text, snippet_text, only_if_exist_emails, only_if_exist_phone_numbers, emails, phone_numbers):
                results.append({
                    "title": title_text,
                    "link": href,
                    "snippet": snippet_text,
                    "emails": list(set(emails)),
                    "phone_numbers": phone_numbers,
                    "metrics": extract_instagram_metrics(snippet_text)
                })

        json_output = json.dumps(results, indent=4)

        with open(current_dir + '/../data/processed/' + text_to_find.replace(' ', '_') + '.json', 'w', encoding='utf-8') as extracted_data_file:
            extracted_data_file.write(json_output)

        print(f"Extracted data saved to {'../data/processed/' + text_to_find.replace(' ', '_') + '.json'}")

    
if __name__ == "__main__":
    text_to_find = "moda feminina"
    pages = 5
    only_if_exist_emails = True
    only_if_exist_phone_numbers = True
    extract_emails_from_instagram_using_duckduckgo_regex(text_to_find, pages, only_if_exist_emails, only_if_exist_phone_numbers)
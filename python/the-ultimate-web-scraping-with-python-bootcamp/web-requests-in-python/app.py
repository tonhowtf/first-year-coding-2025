import requests as r
from bs4 import BeautifulSoup

resp = r.get("https://books.toscrape.com/")

soup = BeautifulSoup(resp.content, "html.parser")

print(soup.ul.prettify)
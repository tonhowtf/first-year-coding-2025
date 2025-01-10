from urllib.request import urlopen

url = "https://quotes.toscrape.com/"

with urlopen(url) as response:
    content = response.read()
    print(content.decode("utf-8"))
import requests

url = "https://quotes.toscrape.com/"


resp = requests.get(url)
# print(resp)

#print(resp.content.decode("utf-8"))

# print(resp.text)

# print(resp.headers)

print(type(resp))

# print(resp.headers)

print(resp.headers['Content-Type'])

resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

resp = requests.get("https://httpbin.org/headers")

print(resp.json())

print(dict(resp.request.headers))
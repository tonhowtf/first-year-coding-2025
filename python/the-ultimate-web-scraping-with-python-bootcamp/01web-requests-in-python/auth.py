import requests as r

API = "Your_API_KEY_here"

url = "https://api.exchange.coinbase.com/fills"

headers = {
    "Authorization": f"Bearer {API}",
    "Content-Type": "application/json"
}

print(r.get(url, headers=headers))


# basic auth -> username, password

auth = ("user1", "pass2")

url = "https://www.httpbin.org/basic-auth/user1/pass2"

print(r.get(url, auth=auth))


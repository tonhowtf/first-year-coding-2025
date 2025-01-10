url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"

import requests as r 

resp = r.get(url)

#print(resp.json()['data']['rates']['USD'])

url = "https://api.coinbase.com/v2/exchange-rates"

params = {"currency": "BTC"}
resp = r.get(url, params=params)
#print(resp.json()['data']['rates']['USD'])


url = "https://api.sunrisesunset.io/json"

params = {
    "lat": "36.7201600", 
    "lng": "-4.4203400", 
    "timezone": "Europe/Madrid,", 
    "date": "today"
}

headers = {
#Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"
}


resp = r.get(url, params=params)

print(resp.status_code)

print(resp.request.url)



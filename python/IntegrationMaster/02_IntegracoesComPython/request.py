import requests


r = requests.get('https://pypi.org')
print(r.status_code)
print(r.text)

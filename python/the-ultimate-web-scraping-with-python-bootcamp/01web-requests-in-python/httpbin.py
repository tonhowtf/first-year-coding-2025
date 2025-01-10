import requests as r

print(r.delete("https://www.httpbin.org/delete").json())

print(r.patch("https://www.httpbin.org/patch").json())
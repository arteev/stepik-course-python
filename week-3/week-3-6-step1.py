import requests

params = {"key": "value"}
r = requests.get("http://example.com", params)
print(r.text)

print(r.url)

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url,cookies = cookies)
print(r.text)

print(r.cookies.items())
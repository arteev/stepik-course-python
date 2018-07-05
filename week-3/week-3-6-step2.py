import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/899.txt'
r = requests.get(url)
lines = r.text.splitlines()
print(len(lines))

import requests


def get(url):
    r = requests.get(url)
    return r.text


base_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
geturl = '699991.txt'

response = ""

jumps = 0
while 'We ' not in geturl:
    jumps += 1
    geturl = get(base_url + "/" + geturl)
    print("[{0:d}] {1:s}".format(jumps, geturl))

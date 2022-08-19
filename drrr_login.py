
# special thanks!: https://gist.github.com/Clavelito/5bd3d316236e5e71f8d3ec033cf644bb

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url_login = "http://drrrkari.com/#"
session = requests.session()

req = session.get(url_login)
soup = BeautifulSoup(req.text, 'html.parser')
token = soup.find('input', attrs={'name': 'token'}).get('value')
cookie = req.cookies

login_info = {
    "language":"jp-JP",
    "icon":"girl",
    "name":"pelu2",
    "login":"login",
    "token":token
}
header = {
    'User-Agent':'w3m'
}

res = session.post(url_login, data=login_info, cookies=cookie, headers=header)
res.raise_for_status()

print(res.text)

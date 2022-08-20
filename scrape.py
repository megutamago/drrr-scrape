import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url_login = "http://drrrkari.com/#"
url_room = "http://drrrkari.com/room/"
url_logout = "http://drrrkari.com/room/#"
session = requests.session()

req = session.get(url_login)
soup = BeautifulSoup(req.text, 'html.parser')
token = soup.find('input', attrs={'name': 'token'}).get('value')
cookie = req.cookies

header = {
    'User-Agent':'w3m'
}

login_info = {
    "language":"jp-JP",
    "icon":"setton",
    "name":"nyahallo",
    "login":"login",
    "token":token
}

room_info = {
    "login":"login",
    "id":"xxxxxxxxxxxxxxxxxxxxx"
}

logout_info = {
        "logout":"退室"
}

session.post(url_login, data=login_info, cookies=cookie, headers=header)
res = session.post(url_room, data=room_info, cookies=cookie, headers=header)
#session.post(url_logout, data=logout_info, cookies=cookie, headers=header)

res.raise_for_status()

soup_2 = BeautifulSoup(res.text, 'html.parser')


contents = soup_2.find_all('dl')
t = [c.get_text() for c in contents]

texts = []
for elem in t:
   news = elem.replace("\n","")
   texts.append(news)

print(*texts, sep='\n')       

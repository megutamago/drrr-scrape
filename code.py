import requests
from bs4 import BeautifulSoup

session = requests.session()

url_login = 'http://drrrkari.com/#'
req_before = session.get(url_login)
cookie_before = req_before.cookies

bs = BeautifulSoup(req_before.text, 'html.parser')
token = bs.find(attrs={'name':'token'}).get('value')

login_info = {
    "language":"jp-JP",
    "icon":"setton",
    "name":"nyaharo",
    "login":"login",
    "token":token
}

url_login = "http://drrrkari.com/#"
res = session.post(url_login, data=login_info)
res.raise_for_status()

res.encoding = res.apparent_encoding 
print(res.text)

f = open('myfile.txt', 'w', encoding='UTF8')
f.write(res.text)
f.close()


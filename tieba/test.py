import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.baidu.com').text
soup = BeautifulSoup(res, 'lxml')
print(soup)
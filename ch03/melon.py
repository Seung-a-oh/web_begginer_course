import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/day/index.htm',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#frm > div > table > tbody > tr')

for tr in trs:
    number = tr.select_one('.rank').text.strip()
    title = tr.select_one('.ellipsis.rank01 > span > a').text
    artist = tr.select_one('.ellipsis.rank02 > span > a').text
    print(number, title, "-", artist)

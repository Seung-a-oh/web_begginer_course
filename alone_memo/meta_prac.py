#크롤링 연습하기
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

og_title = soup.select_one('meta[property="me2:category2"]')['content']
og_img = soup.select_one('meta[property="og:image"]')['content']
og_dec = soup.select_one('meta[property="og:description"]')['content']
print(og_title,og_img,og_dec)
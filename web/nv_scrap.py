
# requests 모듈 -> 웹페이지를 요청하고 응답 데이터를 받을 수 있다.
import requests as req
from bs4 import BeautifulSoup # 뷰티플수프  -> HTML 해석기

response = req.get('https://news.naver.com')
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

content = soup.select('.cnf_news_item')
print(content[0].text)

print("class로 선택, 반복문으로 text 출력")

for c in content:
    print(c.text)
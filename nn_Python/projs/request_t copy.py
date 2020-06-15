import requests
from bs4 import BeautifulSoup

# html 가져오기 성공여부
req_t = requests.get("https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100")

# html.parser: Element, Attribute, Text를 분리 html document
html_t = req_t.content

# print(html_t)
# 뷰티풀숲으로 utf-8 해결
html_bs = BeautifulSoup(html_t, 'html.parser')
# print(html_bs.prettify())

# children 출력
t_li = [item for item in html_bs.children]
print("==t_li[1] ==")
# print(t_li[1])
print("==t_li[3] ==")
# print(t_li[3])

# 텍스트만 출력
tags = t_li[3]
# print(tags.text)
print(tags.get_text())

print(' == end == ')
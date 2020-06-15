import requests
from bs4 import BeautifulSoup 

# html 가져오기 성공여부 
req_t = requests.get("https://www.koreabaseball.com/Player/Register.aspx")

# HTML.PARSER : Element, Attribute, Text를 분리 HTML DOCUMENT
c = req_t.content
print(c)

s = BeautifulSoup(c, "html.parser")
print(s.prettify())

# FIND 메소드로 HEADLINE 목록을 크롤링하여 GET
# s.find("ul", {"class" : "type06_headline"})
#  : ul 태그 중 클래스명이 type06_headline인 것만 찾음 #
pls = s.find("table", {"class" : "tNData"})
print(pls)
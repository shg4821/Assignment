import requests
from bs4 import BeautifulSoup 

# html 가져오기 성공여부 
req_t = requests.get("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100")

# HTML.PARSER : Element, Attribute, Text를 분리 HTML DOCUMENT
c = req_t.content
print(c)

s = BeautifulSoup(c, "html.parser")
print(s.prettify())

# FIND 메소드로 HEADLINE 목록을 크롤링하여 GET
# s.find("ul", {"class" : "type06_headline"})
#  : ul 태그 중 클래스명이 type06_headline인 것만 찾음 #
heads = s.find("ul", {"class" : "type06_headline"})
#print(heads)

# text값 가져오기 
dts = heads.find_all("dt")
# print(dts)
for dt in dts:
    try:
        if not dt.has_attr("class"):
            print("정치 TITLE : ", dt.find("a").text.strip("\r\n").strip())
    except Exception as e:
        print(e.args)

print("== end ==")
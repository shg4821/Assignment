import requests
from bs4 import BeautifulSoup # 볼 수 있게 바꿔줌 

# html 가져오기 성공여부 
req_t = requests.get("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100")

# HTML.PARSER : Element, Attribute, Text를 분리 HTML DOCUMENT
c = req_t.content
# print(c)

s = BeautifulSoup(c, "html.parser")
# print(s.prettify())


#li의 차일드 타입 출력
#t_li = [ item for item in s.children ]
#print("t_li[0]")
#print(t_li[0])
#print("t_li[1]")
#print(t_li[1])
#print("t_li[2]")
#print(t_li[2])
#print("== end ===")

#FIND 메소드를 통해 HEADLINE 목록을 크롤링하여 GET
heads = s.find("ul", {"class": "type06_headline"})

# text 값 출력
dts = heads.find_all("dt")
for dt in dts:
    try:
        if not dt.has_attr("class"):
            print("text :", dt.find("a").text.strip("\r\n").strip())
    except Exception as e:
        print(e.args)

print("== end ==")
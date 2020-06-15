import requests as req 
from bs4 import BeautifulSoup

#
html = req.get("https://www.koreabaseball.com/Player/Search.aspx")
c = html.content

s = BeautifulSoup(c, 'html.parser')

#li의 차일드 타입 출력
t_li = [ item for item in s.children ]
print("t_li[0]")
print(t_li[0])
print("t_li[1]")
print(t_li[1])
print("t_li[2]")
print(t_li[2])
print("== end ===")

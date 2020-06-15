import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

# 파라미터 
page = '1'              # 페이지수 
row = '10'              # 페이지당 목록 수 
sDate = '20200310'      # 조회 시작일 : YYYYMMDD
eDate = '20200422'      # 조회 종료일 : YYYYMMDD
# 파라미터 조합 
params = '&' + 'pageNo=' + page + '&' + 'numOfRows=' + row + '&' + 'startCreateDt=' + sDate + '&' + 'endCreateDt=' + eDate
# API  인증키 
key = 'pheKFj8Pv7Uv7EnJIYCWrt2jBSOo6WalN3YPI08%' + '2FjDXHKtpOthPuS4atzK7C8W2xQv071%' + '2FNJej2ceRkz9T6QYg%3D%3D'

# Open API URL 
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + key + params

req = requests.get(url) 
print(type(req))
html = req.text 
print(type(html)) #이제 string객체로 바꼈다.
print(html) #이렇게 내용물을 확인할 수 있다.

soup = BeautifulSoup(html, 'html.parser')
finded_values = soup.find_all('item')
[x.text for x in finded_values]


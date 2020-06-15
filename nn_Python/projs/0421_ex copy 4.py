import json
import urllib.request as ul
import xml.etree.ElementTree as et
import requests 
import os
import sys
import collections
from bs4 import BeautifulSoup 
import os.path as path
import pymongo
from pymongo import MongoClient


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

# ET 
response = requests.get(url)
status = response.status_code
text = response.text
root = et.fromstring(response.text)
result = root.tag

print(root)

# request
rq = requests.get(url)
# print(rq)
# BeautifulSoup
bs = BeautifulSoup(rq.content, 'html.parser')
#print(bs)
# item
data = bs.find_all('item')
print(data)

for item in data:
    # print(data)
    createDt = item.find('createDt')
    examCnt = item.find('examCnt')                  # 검사 진행
    decideCnt = item.find('decideCnt')              # 확진자
    careCnt = item.find('careCnt')                  # 치료중 
    clearCnt = item.find('clearCnt')                # 격리 해제 
    deathCnt = item.find('deathCnt')                # 사망자  
    resutlNegCnt = item.find('resutlNegCnt')
    print(createDt.text)
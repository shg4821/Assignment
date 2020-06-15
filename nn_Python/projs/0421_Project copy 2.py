import json
import os
import sys
import urllib.request
import collections
import pymongo
from pymongo import MongoClient
from xml.dom import minidom
from xml.etree import ElementTree

cnts = []                   # 카운팅
stateDts = []               # 기준일자
stateTimes = []             # 기준시각
examCnts = []               # 검사 진행
decideCnts = []             # 확진자
clearCnts = []              # 격리 해제 
careCnts = []               # 치료중
deathCnts = []              # 사망자

# 스트링을 받아 특정기호를 제거해 주는 함수
def remove_any(pTarget, pChars):
    for c in pChars:
            pTarget = pTarget.replace(c, '')
    return pTarget


# 파라미터 
page = '1'              # 페이지수 
row = '10'              # 페이지당 목록 수 
sDate = '20200310'      # 조회 시작일 : YYYYMMDD
eDate = '20200504'      # 조회 종료일 : YYYYMMDD
# 파라미터 조합 
params = '&' + 'pageNo=' + page + '&' + 'numOfRows=' + row + '&' + 'startCreateDt=' + sDate + '&' + 'endCreateDt=' + eDate
# API  인증키 
key = 'pheKFj8Pv7Uv7EnJIYCWrt2jBSOo6WalN3YPI08%' + '2FjDXHKtpOthPuS4atzK7C8W2xQv071%' + '2FNJej2ceRkz9T6QYg%3D%3D'

# Open API URL 
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + key + params

print(url)
# json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
 
    #xml 도큐먼트 
    root = ElementTree.fromstring(response_body)
    # xmldoc = ElementTree.dump(root)
    #print(root.tag)
    #for child in root:
    #  print(child.tag, child.attrib)
    #print(root[0][0])
    #print(root[0][0].text)
    #print(root[0].findall("item"))
    #print(root[0].find("title").text)
    #print(root[0].find("item")[0].text)
    print(type(root.findall("item")))
    lists = root[0].findall("item")
    word = []
    for obj in lists:
        print(obj.find("title").text)
        word = remove_any(obj.find("title").text, ['\n','&quot;','.',',',',',"'","‘","’","[","]","→","/","&gt","…","·",'“','”','&lt;',';','!','?','</b>','<b>','(',')','⑫','...'])
        words.extend(word.split(' '))
    print(words)
else:
    print("Error Code:" + rescode)
    # 반복문으로 출력
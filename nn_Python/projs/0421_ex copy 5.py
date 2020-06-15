from urllib.request import urlopen
from xml.etree import ElementTree as et
import pandas as pd 
import sys

import collections
from xml.dom import minidom

rows = []

# 파라미터 
page = '1'              # 페이지수 
row = '10'              # 페이지당 목록 수 
sDate = '20200310'      # 조회 시작일 : YYYYMMDD
eDate = '20200506'      # 조회 종료일 : YYYYMMDD
# 파라미터 조합 
params = '&' + 'pageNo=' + page + '&' + 'numOfRows=' + row + '&' + 'startCreateDt=' + sDate + '&' + 'endCreateDt=' + eDate
# API  인증키 
key = 'pheKFj8Pv7Uv7EnJIYCWrt2jBSOo6WalN3YPI08%2FjDXHKtpOthPuS4atzK7C8W2xQv071%2FNJej2ceRkz9T6QYg%3D%3D'

# Open API URL 
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + key + params + ".xml"

#response = urlopen(url).read()
#xtree = et.fromstring(response)



rows = []
#for n in xtree:
    #n_cdate = n.find("createDt").text
    #n_decide = n.find("decideCnt").text
    #n_exam = n.find("examCnt").text
    #n_care = n.find("careCnt").text
    #n_clear = n.find("clearCnt").text
    #rows.append({"생성일자": n_cdate, "확진자":n_decide, "검사진행":n_exam, "치료중":n_care, "완치":n_clear})



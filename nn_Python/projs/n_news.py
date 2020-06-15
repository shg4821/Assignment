import os
import sys
import urllib.request
import json
client_id = "ARmOA74jXwrC79uUhwdp"
client_secret = "y2HM_tbj9T"
encText = urllib.parse.quote("영화")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

# 스트링을 받아 특정 기호를 제거해주는 함수 
def remove_any(pTarget, pChars):
    for c in pChars:
        pTarget = pTarget.replace(c, '')
    return pTarget

# 불필요한 것들 제거한 단어들을 리스트로 추가 
words = []
# 요청 확인 
if(rescode==200): # 성공
    response_body = response.read()
    u8_json = response_body.decode('utf-8')
    # 파이썬 json객체로 변경
    j = json.loads(u8_json)
    
    # 반복문으로 출력 
    # 변수 선언 
    word = []
    for it in j["items"]:
        #단어 외의 불필요한 요소 제거
        word = remove_any(it["title"], ['\n', '&quot;',',','[포토]','<b>','</b>', '...','[',']', '…','(',')',
        '..',"'", '"', '&lt;', '&gt;','‘','’', '|', '/','“','”','!','★',''])
        # word 스트링을 words 배열에 추가 
        # extend 배열 a.extend(배열 b) : 배열 a와 배열 b를 하나의 배열로 만들어줌 
        words.extend(word.split(' '))
    print(words)
else:
    print("Error Code:" + rescode)


# 빈도수가 제일 높은 단어 
# words 중 가장 
print(max(words, key=words.count))
print("== End ==")
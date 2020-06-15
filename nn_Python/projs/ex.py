import json
import os
import sys
import urllib.request
import collections
import pymongo
from pymongo import MongoClient

def doFiles():
    words = []
    # 스트링을 받아 특정기호를 제거해 주는 함수
    def remove_any(pTarget, pChars):
        for c in pChars:
                pTarget = pTarget.replace(c, '')
        return pTarget

    # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴
    def getNavMovie(mKey):
        client_id = "ARmOA74jXwrC79uUhwdp"
        client_secret = "y2HM_tbj9T"

        # 파라미터
        encText = "&".join(["query="+urllib.parse.quote(mKey)
        , "display=100"
        , "start=1"
        ])
        url = "https://openapi.naver.com/v1/search/movie?" + encText

        # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            #print(response_body.decode('utf-8'))
            # json
            u8_json = response_body.decode('utf-8')
            # 파이썬 json 객체
            j = json.loads(u8_json)

            # 반복문으로 출력

            word = []
            for it in j["items"]:
                word = remove_any(it["title"], ['\n','&quot;','.',',',',',"'","‘","’","[","]","→","/","&gt","…","·",'“','”','&lt;',';','!','?','</b>','<b>','(',')','⑫','...'])
                words.extend(word.split(' '))
            print(words)
            return words
        else:
            print("Error Code:" + rescode)

    def insertMongo(pWords):

        # 몽고디비 연결 클라이언트
        # 1.몽고디비 클라이언트 연결객체 생성
        cl = MongoClient('mongodb://localhost:27017/')
        # -- 객체생성확인
        print('client.HOST: {0}'.format(cl.HOST))

        # 2. 데이터베이스 생성
        gdb = cl['gdb_py']
        # -- 디비 생성 확인
        print(gdb)

        # 3. 컬렉션 객체 생성
        gdb.keys.remove()
        keys = gdb.keys

        keys_cs = [ {'words': pWords} ]

        #5. 여러개의 데이터 입력
        rst_keys = keys.insert_many(keys_cs)
        print(rst_keys)

    #for it in words:
    #    print(it)
    
    

    menus = ['Exit', 'Save', 'Load', 'Save & Load']
    sel_index = 0
    print("== START! ==")
    while True:
        # 메뉴출력
        print('== MENU ==')
        for m in range(0, len(menus)):
            print('%d.%s' % (m, menus[m]))

        sel_index = input('Choice : ')

        # 선택별 진행
        if sel_index == '0':
            print("== THE END ==")
            break
        elif sel_index != '0': # 등록인경우
            mKey = input('Search : ')
            # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴하는 함수 getNavMovie()을 실행
            words = getNavMovie(mKey)
            insertMongo(words)

# 프로그램 실행
doFiles()

print(" == ALL END == ")
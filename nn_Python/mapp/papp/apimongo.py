import json
import os
import sys
import urllib.request
import collections
import pymongo
from pymongo import MongoClient
from xml.dom import minidom
from xml.etree import ElementTree
from collections import Counter
from bson.json_util import dumps

def doNavApi(pKey, pColname):
    words = []
    # 스트링을 받아 특정기호를 제거해 주는 함수
    def remove_any(pTarget, pChars):
        for c in pChars:
                pTarget = pTarget.replace(c, '')
        return pTarget

    # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴
    def getNavNews(pKey):
        client_id = "ARmOA74jXwrC79uUhwdp"
        client_secret = "y2HM_tbj9T"

        # 파라미터
        encText = "&".join(["query="+urllib.parse.quote(pKey)
        , "display=100"
        , "start=1"
        ])
        url = "https://openapi.naver.com/v1/search/news?" + encText

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
        client = MongoClient('mongodb://localhost:27017/')
        # -- 객체생성확인
        print('client.HOST: {0}'.format(client.HOST))

        # 2. 데이터베이스 생성
        mdb = client['mdb3_py']
        # -- 디비 생성 확인
        print(mdb)

        # 3. 컬렉션 객체 생성
        mdb[pColname].remove()
        keys = mdb[pColname]

        keys_cs = [ {'words': pWords} ]

        #5. 여러개의 데이터 입력
        rst_keys = keys.insert_many(keys_cs)
        print(rst_keys)

    # 스크래핑후 몽고db저장
    words = getNavNews(pKey)
    insertMongo(words)

    return words

# api 의 결과를 xml로 받기
def doNavApiXml(pKey, pColname):
    words = []
    # 스트링을 받아 특정기호를 제거해 주는 함수
    def remove_any(pTarget, pChars):
        for c in pChars:
                pTarget = pTarget.replace(c, '')
        return pTarget

    # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴
    def getNavNews(pKey):
        client_id = "pVMk3w9kVJJdkLAuxCvn"
        client_secret = "Y5uBH6P1uU"
        encText = urllib.parse.quote(pKey)
        url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            #print(response_body.decode('utf-8'))

            # xml 도큐먼트
            root = ElementTree.fromstring(response_body)
            # dump
            # xmldoc = ElementTree.dump(root)
            #print(root.tag)
            #for child in root:
            #    print(child.tag, child.attrib)
            #print(root[0][0])
            #print(root[0][0].text)
            #print(root[0].findall("item"))
            #print(root[0].find("title").text)
            #print(root[0].find("item")[0].text)
            #print(type(root.findall("item")))
            lists = root[0].findall("item")
            word = []
            for obj in lists:
                print(obj.find("title").text)
                word = remove_any(obj.find("title").text, ['\n','&quot;','.',',',',',"'","‘","’","[","]","→","/","&gt","…","·",'“','”','&lt;',';','!','?','</b>','<b>','(',')','⑫','...'])
                words.extend(word.split(' '))
            print(words)
            return words
        else:
            print("Error Code:" + rescode)
            # 반복문으로 출력

    def insertMongo(pWords):

        # 몽고디비 연결 클라이언트
        # 1.몽고디비 클라이언트 연결객체 생성
        client = MongoClient('mongodb://localhost:27017/')
        # -- 객체생성확인
        print('client.HOST: {0}'.format(client.HOST))

        # 2. 데이터베이스 생성
        mdb = client['mdb_py']
        # -- 디비 생성 확인
        print(mdb)

        # 3. 컬렉션 객체 생성
        mdb[pColname].remove()
        keys = mdb[pColname]

        keys_cs = [ {'words': pWords} ]

        #5. 여러개의 데이터 입력
        rst_keys = keys.insert_many(keys_cs)
        print(rst_keys)

    # 스크래핑후 몽고db저장
    words = getNavNews(pKey)
    insertMongo(words)

    return words

def doNavMov(mKey, mColname):
    words = []
    # 스트링을 받아 특정기호를 제거해 주는 함수
    def remove_any(mTarget, mChars):
        for c in mChars:
                mTarget = mTarget.replace(c, '')
        return mTarget

    # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴
    def getNavMov(mKey):
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
                word = remove_any(it["title"], ['\n','&quot;','.',',',',',"'","‘","’","[","]","→","/","&gt","…","·",'“','”','&lt;',';','!','?','</b>','<b>','(',')','⑫','...','-',"",''," ",":"])
                words.extend(word.split(' '))
            print(words)           
            return words
        else:
            print("Error Code:" + rescode)
    
    def insertMongo(mWords):

        # 몽고디비 연결 클라이언트
        # 1.몽고디비 클라이언트 연결객체 생성
        client = MongoClient('mongodb://localhost:27017/')
        # -- 객체생성확인
        print('client.HOST: {0}'.format(client.HOST))

        # 2. 데이터베이스 생성
        gdb = client['gdb_m_py']
        # -- 디비 생성 확인
        print(gdb)

        # 3. 컬렉션 객체 생성
        gdb[mColname].remove()
        keys = gdb[mColname]

        keys_ms = [ {'words': mWords} ]

        #5. 여러개의 데이터 입력
        r_keys = keys.insert_many(keys_ms)
        print(r_keys)

    # 스크래핑후 몽고db저장
    words = getNavMov(mKey)
    insertMongo(words)

    return words

def insertUserid(pUserid):
    # 몽고디비 연결 클라이언트
    # 1.몽고디비 클라이언트 연결객체 생성
    client = MongoClient('mongodb://localhost:27017/')
    # -- 객체생성확인
    print('client.HOST: {0}'.format(client.HOST))
    # 2. 데이터베이스 생성
    mdb = client['djangodb']
    # -- 디비 생성 확인
    print(mdb)
    # 3. 컬렉션 객체 생성
    # mdb[pColname].remove()
    keys = mdb['useridc']
    _id ={'_id': pUserid}
    #5. 여러개의 데이터 입력
    keys.insert_one(_id)

# 주소정보 몽고디비에 저장
def insertAddrs(pJson):
    # 몽고디비 연결 클라이언트
    # 1.몽고디비 클라이언트 연결객체 생성
    client = MongoClient('mongodb://localhost:27017/')
    # -- 객체생성확인
    print('client.HOST: {0}'.format(client.HOST))
    # 2. 데이터베이스 생성
    mdb = client['djangodb']
    # -- 디비 생성 확인
    print(mdb)
    # 3. 컬렉션 객체 생성
    # mdb[pColname].remove()
    keys = mdb['addrs']
    #5. 여러개의 데이터 입력
    keys.insert_one(pJson)

# 도로명 API 결과를 JSON으로 받기
# http://www.juso.go.kr/addrlink/jusoSearchSolutionIntroduce.do
def doJusoApi(request, pKey):
    # 초기
    pKey = urllib.parse.quote(pKey)
    cKey = "devU01TX0FVVEgyMDIwMDUyMDE2MDk1MzEwOTc3OTI="
    url = "http://www.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=10&keyword="+pKey+"&confmKey=" + cKey + "&resultType=json"
    # 주소 json 결과 받기 :
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        # 주소 json 결과 처리 :
        response_body = response.read()
        # 파이썬 json 객체
        u8_json = response_body.decode('utf-8')
        j = json.loads(u8_json)
        roadAddr = []
        #print(j)
        for it in j["results"]["juso"]:
            roadAddr.append(it['roadAddr'])
        print(roadAddr)
    else:
        print("Error Code:" + rescode)
    return roadAddr

# 예전의 doFile : API 결과를 JSON으로 받기
def doNavApi2(pKey, pColname):
    words = []
    
    # 스트링을 받아 특정기호를 제거해 주는 함수
    def remove_any(pTarget, pChars):
        for c in pChars:
            pTarget = pTarget.replace(c, '')
        return pTarget

    # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴
    def getNavNews(pKey):
        client_id = "ARmOA74jXwrC79uUhwdp"
        client_secret = "y2HM_tbj9T"

        # 파라미터
        encText = "&".join(["query="+urllib.parse.quote(pKey)
        , "display=100"
        , "start=1"
        ])
        url = "https://openapi.naver.com/v1/search/news?" + encText

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
            #print(words)
            json_list = Counter(words)
            json_list = json_list.most_common(10)
            for wd in json_list:
                print(wd)
            return words
        else:
            print("Error Code:" + rescode)

    def insertMongo(pWords):

        # 몽고디비 연결 클라이언트
        # 1.몽고디비 클라이언트 연결객체 생성
        client = MongoClient('mongodb://localhost:27017/')
        # -- 객체생성확인
        print('client.HOST: {0}'.format(client.HOST))

        # 2. 데이터베이스 생성
        mdb = client['hgdb']
        # -- 디비 생성 확인
        print(mdb)

        # 3. 컬렉션 객체 생성
        mdb[pColname].remove()
        keys = mdb[pColname]

        keys_cs = [ {'words': pWords} ]

        #5. 여러개의 데이터 입력
        keys.insert_many(keys_cs)
        #print(rst_keys)

    # 스크래핑후 몽고db저장
    words = getNavNews(pKey)
    insertMongo(words)

    return words

# 디비의 컬렉션의 도큐먼트 가져오기
def selDocument(theme_sel):
    # 몽고디비 연결 클라이언트
    # 1.몽고디비 클라이언트 연결객체 생성
    client = MongoClient('mongodb://localhost:27017/')
    # -- 객체생성확인
    print('client.HOST: {0}'.format(client.HOST))
    # 2. 데이터베이스 생성
    mdb = client['hgdb']
    # -- 디비 생성 확인
    docs = dumps(mdb[theme_sel].find())
    print(docs)
    return docs

# 디비의 컬렉션 목록 가져오기
def selCollection():
    # 몽고디비 연결 클라이언트
    # 1.몽고디비 클라이언트 연결객체 생성
    client = MongoClient('mongodb://localhost:27017/')
    # -- 객체생성확인
    print('client.HOST: {0}'.format(client.HOST))
    # 2. 데이터베이스 생성
    mdb = client['hgdb']
    # -- 디비 생성 확인
    print(mdb.list_collection_names())
    return mdb.list_collection_names()


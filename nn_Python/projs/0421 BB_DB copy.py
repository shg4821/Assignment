import json
import requests
from bs4 import BeautifulSoup 
import os.path as path
import collections
import pymongo
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup 
import os.path as path

menu = ['나가기', '타자기록', '투수기록', '수비기록', '주루기록']
h_tabs = ['순위', '선수명', '타율', '안타', '홈런', '타점']
p_tabs = ['순위', '선수명', '평자책점', '승률', '이닝수', 'WHIP']
d_tabs = ['순위', '선수명', '포지션', '선발경기', '이닝수', '수비율']
r_tabs = ['순위', '선수명', '경기수', '도루시도', '도루허용', '도루성공율']
sel_index = 0

# html 가져오기 성공여부
# 타자
rh = requests.get("https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx")
# 투수
rp = requests.get("https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx")
# 수비
rd = requests.get("https://www.koreabaseball.com/Record/Player/Defense/Basic.aspx")
# 주루
rr = requests.get("https://www.koreabaseball.com/Record/Player/Runner/Basic.aspx")

# html.parser: Element, Attribute, Text를 분리 html document
# 뷰티풀숲
hitR = BeautifulSoup(rh.content, 'html.parser')
pitR = BeautifulSoup(rp.content, 'html.parser')
defR = BeautifulSoup(rd.content, 'html.parser')
runR = BeautifulSoup(rr.content, 'html.parser')


# FIND 
h = hitR.find('table', { 'class': 'tData01 tt' })  #<table class ="tData01 tt">을 찾음
p = pitR.find('table', { 'class': 'tData01 tt' })
d = defR.find('table', { 'class': 'tData01 tt' })
r = runR.find('table', { 'class': 'tData01 tt' })

h_data = []                                 # 데이터 리스트 생성
for tr in h.find_all('tr'):                 # 모든 <tr> 태그를 찾아서 반복( 각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))           # 모든 <td> 태그를 찾아서 리스트로 만듦
    for td in tds:                          #<td> 태그 리스트 반복(각 세부 기록을 가져옴)
        if td.find('a'):                    
            player = td.find('a').text      # <a> 선수 이름
            avg = tds[3].text               # 인덱스 3 타율
            h = tds[8].text                 # 인덱스 8 안타
            hr = tds[11].text               # 인덱스 11 홈런.
            RBI = tds[13].text              # 인덱스 13 타점
            h_data.append([player, avg, h, hr, RBI])   #dat 리스트에 선수, 타율, 안타를 추가
h_data

p_data = []                                 # 데이터 리스트 생성
for tr in p.find_all('tr'):                 # 모든 <tr> 태그를 찾아서 반복( 각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))           # 모든 <td> 태그를 찾아서 리스트로 만듦
    for td in tds:                          #<td> 태그 리스트 반복(각 세부 기록을 가져옴)
        if td.find('a'):                    
            player = td.find('a').text      # <a> 선수 이름
            era = tds[3].text               # 평자책점
            wpct = tds[9].text              # 승률
            ip = tds[10].text               # 이닝수
            whip = tds[18].text             # 이닝당 출루 허용률
            p_data.append([player, era, wpct, ip, whip])

d_data = []                                 # 데이터 리스트
for tr in d.find_all('tr'):                 # 모든 <tr> 태그를 찾아서 반복( 각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))           # 모든 <td> 태그를 찾아서 리스트로 만듦
    for td in tds:                          # <td> 태그 리스트 반복(각 세부 기록을 가져옴)
        if td.find('a'):                    
            player = td.find('a').text      # <a> 선수 이름
            pos = tds[3].text               # 포지션
            gs = tds[5].text                # 선발 경기수
            dip = tds[6].text               # 수비 이닝수
            fpct = tds[12].text             # 수비율
            d_data.append([player, pos, gs, dip, fpct])   #dat 리스트에 선수, 타율, 안타를 추가
d_data

r_data = []                                 # 데이터 리스트 생성
for tr in r.find_all('tr'):                 # 모든 <tr> 태그를 찾아서 반복( 각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))           # 모든 <td> 태그를 찾아서 리스트로 만듦
    for td in tds:                          # <td> 태그 리스트 반복(각 세부 기록을 가져옴)
        if td.find('a'):                    
            player = td.find('a').text      # <a> 선수 이름
            rg = tds[3].text                # 경기수
            sba = tds[4].text               # 도루시도
            sb = tds[5].text                # 도루허용
            sbp = tds[7].text               # 성공율
            r_data.append([player, rg, sba, sb, sbp])

# ==================== 파일 =========================
# 타자
def h_save():
    with open('2019_hitter.txt', 'w', encoding='utf-8') as file:
        file.write('player, avg, h, hr, RBI\n')
        # 컬럼 이름 추가
        for hd in h_data:
            file.write('{0},{1},{2},{3},{4}\n'.format(hd[0], hd[1], hd[2], hd[3],hd[4]))
            # 선수이름,타율,안타수를 줄 단위로 저장

# 투수
def p_save():
    with open('2019_pitcher.txt', 'w', encoding='utf-8') as file:
        file.write('player, era, wpct, ip, whip\n')
        for pd in p_data:
            file.write('{0},{1},{2},{3},{4}\n'.format(pd[0], pd[1], pd[2], pd[3],pd[4]))

# 수비
def d_save():
    with open('2019_defense.txt', 'w', encoding='utf-8') as file:
        file.write('player, pos, gs, dip, fpct\n')
        for dd in d_data:
            file.write('{0},{1},{2},{3},{4}\n'.format(dd[0], dd[1], dd[2], dd[3],dd[4]))

# 주루
def r_save():
    with open('2019_runner.txt', 'w', encoding='utf-8') as file:
        file.write('player, rg, sba, sb, sbp\n')
        for rd in r_data:
            file.write('{0},{1},{2},{3},{4}\n'.format(rd[0], rd[1], rd[2], rd[3],rd[4]))


def hitter():
    print("     ".join(h_tabs))
    for hd in range(0, len(h_data)):
        print('%d   %s' % (hd+1, h_data[hd]))
    print('== List End ==')
    h_save()
    print('SAVE COMPLETE !')

def pitcher():
    print("     ".join(p_tabs))
    for pd in range(0, len(p_data)):
        print('%d   %s' % (pd+1, p_data[pd]))
    p_save()
    print('SAVE COMPLETE !')

def defense():
    print("     ".join(d_tabs))
    for dd in range(0, len(d_data)):
        print('%d   %s' % (dd+1, d_data[dd]))
    d_save()
    print('SAVE COMPLETE !')

def runner():
    print("     ".join(r_tabs))
    for rd in range(0, len(r_data)):
        print('%d   %s' % (rd+1, r_data[rd]))
    r_save()
    print('SAVE COMPLETE !')
    



# 프로그램 실행 
print('== Program Start ! == ')
while True:
    # 메뉴 출력 
    print('== MENU LIST ==')
    for m in range(0, len(menu)):
        print('%d.%s' % (m, menu[m]))
    sel_index = int(input('CHOICE : '))

    # 선택별 진행 
    if sel_index == 0: 
        break 
    elif sel_index == 1: 
        hitter()
    elif sel_index == 2:
        pitcher()
    elif sel_index == 3: 
        defense()
    elif sel_index == 4: 
        runner()


def doFiles():
    words = []
    # 스트링을 받아 특정기호를 제거해 주는 함수
    def remove_any(pTarget, pChars):
        for c in pChars:
                pTarget = pTarget.replace(c, '')
        return pTarget

    # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴
    def getNavNews(pKey):
        client_id = ""
        client_secret = ""

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
        mdb = client['mdb_py']
        # -- 디비 생성 확인
        print(mdb)

        # 3. 컬렉션 객체 생성
        mdb.keys.remove()
        keys = mdb.keys

        keys_cs = [ {'words': pWords} ]

        #5. 여러개의 데이터 입력
        rst_keys = keys.insert_many(keys_cs)
        print(rst_keys)

    #for it in words:
    #    print(it)
    
    

    menus = ['나가기', '데이터저장', '불러오기', '데이터저장&불러오기']
    sel_index = 0
    print("== TEST START! ==")
    while True:
        # 메뉴출력
        print('== MENU LIST ==')
        for m in range(0, len(menus)):
            print('%d.%s' % (m, menus[m]))

        sel_index = input('CHOICE : ')

        # 선택별 진행
        if sel_index == '0':
            print("== THE END ==")
            break
        elif sel_index != '0': # 등록인경우
            vKey = input('키워드 : ')
            # 네이버에서 가져온 데이터를 단어로 분리해 배열로 리턴하는 함수 getNavNews()을 실행
            words = getNavNews(vKey)
            insertMongo(words)

# 프로그램 실행
doFiles()

print(" == ALL END == ")
import requests
from bs4 import BeautifulSoup 
import numpy as np


m = ['나가기', '타자기록', '투수기록', '수비기록', '주루기록']
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
hitter = rh.content
pitcher = rp.content
defense = rd.content
runner = rr.content

# print(html_t)
# 뷰티풀숲으로 utf-8 해결
hitR = BeautifulSoup(hitter, 'html.parser')
pitR = BeautifulSoup(pitcher, 'html.parser')
defR = BeautifulSoup(defense, 'html.parser')
runR = BeautifulSoup(runner, 'html.parser')

# FIND 대신 select 사용
h = hitR.select('.tData01 td')
p = pitR.select('.tData01 td')
d = defR.select('.tData01 td')
r = runR.select('.tData01 td')
print(h)
# print(p)

# 태그 제거 
for td in h:
	hRec = print(td.text('  '))

# 불필요한 것들 제거한 단어들을 리스트로 추가 
tabs = ['순위', '선수명', '팀명', 'AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI', 'SAC', 'SF']
records = []

records = [item.get_text().strip() for item in hitR.select('td')]

print(records)

records = np.array(records)
records.resize(len(tabs), 30)



def r_hitter():
    print(tabs)
    for td in h:
        print(hRec)

def r_pitcher():
    print(tabs)


def r_defense():
    print(tabs)


def r_runner():
    print(tabs)


print("     ".join(map(str, tabs)))


while True:
    # 메뉴 출력 
    print('== MENU LIST ==')
    for m in range(0, len(m)):
        print('%d.%s' % (m, m[m]))
    sel_index = int(input('선택 : '))

    # 선택별 진행 
    if sel_index == 0: 
        break 
    elif sel_index == 1: 
        r_hitter()
    elif sel_index == 2:
        r_pitcher()
    elif sel_index == 3: 
        r_defense()
    elif sel_index == 3: 
        r_runner()











# 등록함수 
def append_h():
    h_data.append([player, avg, h, hr, RBI])
def append_p():
    p_data.append([player, era, wpct, ip, whip])
def append_d():
    d_data.append([player, pos, gs, dip, fpct])
def append_r():
    r_data.append([player, rg, sba, sb, sbp])

# 목록 함수 
def list_h():
    for h in h_data:
        print("● %s" % h.replace('\n', ''))
        
def list_p():
    for p in p_data:
        print("● %s" % p.replace('\n', ''))


def list_d():
    for d in d_data:
        print("● %s" % d.replace('\n', ''))


def list_r():
    for r in r_data:
        print("● %s" % r.replace('\n', ''))

# 파일을 읽어와서 컬렉션에 추가 (컬렉션 : 배열 ) 
def read_mov():
    global movies
    if path.exists(file_path): # 파일 존재여부 확인 
        f = open(file_path, 'r', encoding='utf-8')
        movies = f.readlines()

# 파일 저장하기 함수 
def save_mov():
    global movies
    f = open(file_path, 'w', encoding='utf-8')
    movies = '\n'.join(movies)
    f.writelines(movies)
    print('SAVE COMPLETE !')






while True:
    # 메뉴 출력 
    print('== MENU LIST ==')
    for m in range(0, len(m)):
        print('%d.%s' % (m, m[m]))
    sel_index = int(input('선택 : '))

    # 선택별 진행 
    if sel_index == 0: 
        break 
    elif sel_index == 1: 
        r_hitter()
    elif sel_index == 2:
        r_pitcher()
    elif sel_index == 3: 
        r_defense()
    elif sel_index == 4: 
        r_runner()
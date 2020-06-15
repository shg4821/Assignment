import os.path as path

# 초기
movies = []
menus = ['나가기', '등록', '목록', '저장']
sel_index = 0
file_path = 'D:/projs/movies.txt'

# 등록함수 
def append_mov():
    movies.append(input("MOVIE : "))

# 목록 함수 
def list_mov():
    for m in movies:
        print("● %s" % m.replace('\n', ''))

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

# 프로그램 실행 
read_mov()
while True:
    # 메뉴 출력 
    print('== MENU LIST ==')
    for m in range(0, len(menus)):
        print('%d.%s' % (m, menus[m]))
    sel_index = int(input('CHOICE : '))

    # 선택별 진행 
    if sel_index == 0: 
        break 
    elif sel_index == 1: 
        append_mov()
    elif sel_index == 2:
        list_mov()
    elif sel_index == 3: 
        save_mov()



print('== END ==')
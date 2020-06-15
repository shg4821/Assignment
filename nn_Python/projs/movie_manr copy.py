# name_manager.py
import os.path as path

# 초기
def doFiles():
    names = []
    # 등록함수
    def append_name():
        names.append(input('NAME : '))
    
    # 목록함수
    def list_name():
        for n in names:
            print('- %s' % n.replace('\n',''))
    
    #파일을 읽어와서 컬렉션에 추가 함수
    def read_names():
        if path.exists(file_path):
            f = open(file_path, 'r', encoding='utf-8')
            f_names = f.readlines()
            for m in range(0, len(f_names)):
                names.append(f_names[m].replace('\n', ''))
        
    # 파일 저장하기 함수
    def save_names():
        f = open(file_path, 'w', encoding='utf-8')
        f.writelines('\n'.join(names))
        print('COMPLETE SAVE==') 
    
    menus = ['나가기', '등록', '목록', '저장']
    sel_index = 0
    file_path = 'D:/projs/names.txt'

    read_names()
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
        elif sel_index == '1': # 등록인경우
            append_name()
        elif sel_index == '2': # 목록인경우
            list_name()
        elif sel_index == '3': # 저장인경우
            save_names()
 
# 프로그램 실행
doFiles()
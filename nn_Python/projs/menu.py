# 메뉴 선택 

# 초기 
menus = ['나가기', '등록', '목록']

# 입력
print('메뉴 선택 (ex_1번 메뉴 회원번호 107번 : 1 107) <0. 나가기 1. 등록 2. 목록> : ')
cmd = input('COMMAND : ').split()

# 출력
print('메뉴번호 : ', cmd[0], '회원번호 : ', cmd[1])
print('메뉴번호 : %s / 회원번호 : %s' %(cmd[0], cmd[1]))
print('메뉴번호 : {}, 회원번호 : {}'.format(cmd[0], cmd[1]))
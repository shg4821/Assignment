# range 함수 
# range(시작위치, [종료위치,] 증가값)

def printC(dt):
    for idx in range(len(dt)-1, -1, -1):
        yield dt[idx]
    
for char in printC('김바보'):
    print(char)

print('== 종료 ==')
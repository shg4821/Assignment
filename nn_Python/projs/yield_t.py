# 호출시 yield의 순서대로 리턴
def doGen():
    yield '김바보'
    yield '이웃사람'
    yield '마동석'

g = doGen()
print('감독 : '+ next(g))
print('영화 : '+ next(g))
print('배우 : '+ next(g))
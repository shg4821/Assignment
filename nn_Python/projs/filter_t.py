# filter 함수 

#1. 변수 
nums = []
num = None

#짝수 판별 
def is_even(x):
    return x % 2 == 0

# 홀수 판별 
def is_odd(x):
    return x % 2 == 1

# 입력 
while True:
    num = input('수(입력 중지 = 엔터) : ')
    if num == '':
        break 
    nums.append(int(num))
    # 출력 
    print('== 입력수 분석')
    print('짝수 : %s' % list(filter(is_even, nums)))
    print('홀수 : %s' % list(filter(is_odd, nums)))
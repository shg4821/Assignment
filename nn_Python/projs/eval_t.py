# 1. 입력 
in_data = input('수식 : ')

# 2. 출력 
# '1+6' = 문자열 / eval('1+6') = 1+6 수식으로 변환 
print('%s = %d' %(in_data, eval(in_data)))
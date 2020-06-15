# for~ in ~ :
# 구구단 출력 
#  #

# 단출력
def pdan(dan):
    print(dan, "단")

# 수식 출력 
def pexp(num1, num2):
    print(num1, " x ", num2, "=", num1*num2)

#구구단 출력
for i in range(1, 20):
    #단 출력 
    pdan(i)
    for j in range(1, 20):
        pexp(i,j)
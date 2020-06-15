# 변수
def testScope():
    def do_local():
        # 로컬 변수
        food = "로컬푸드"
    
    def do_nonlocal():
        # nonlocal 선언
        nonlocal food
        food = "넌로컬푸드"
    
    def do_global():
        #global 선언
        global food 
        food = "글로벌 푸드"

    food = "샘플푸드"

    do_local()
    print("로컬에서 food 변경 후 : ", food)
    do_nonlocal()
    print("넌로컬에서 food변경 후 - ", food)
    do_global()
    print("글로벌에서 food변경 후 - ", food)

testScope()
print("In global scope:", food)
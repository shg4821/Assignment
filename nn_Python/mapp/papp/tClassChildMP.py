from papp.tClass import tClassName
from papp.tClassOtP import tClassOtParent

# class tClassChildCMParent(부모클래스 목록):
class tClassChildCMParent(tClassName, tClassOtParent):
    # 어트리뷰트
    vChildMParent = 888

    # 초기화 비헤비어 
    # def __init__(self, 부모클래스 매개변수 목록):
    def __init__(self, pParent1, pParent2):
        # 상속초기화 : __init__ ( java의 static )
        tClassName.__init__(self, pParent1)
        tClassOtParent.__init__(self, pParent2)
    
    # 비헤비어
    def testChildMParent():
        a = 2
        b = 10
        return b-a

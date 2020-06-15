import re
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.views.generic import CreateView
from django.http import JsonResponse
import json
from papp.apimongo import doNavApi, doNavApiXml, doNavMov, insertUserid, doJusoApi, insertAddrs, selCollection, selDocument, doNavApi2
from collections import Counter
from sklearn.linear_model import LinearRegression
from papp.tClass2 import tClassName2
from papp.tClass import tClassName
from papp.tClassOtP import tClassOtParent
from papp.tClassChildMP import tClassChildCMParent as cmp
from papp.ChildMP_I import ClassChildCMParent_I as cmpi
from papp.form_.loginFrm import LoginFrm
from papp.form_.jusoFrm import jusoF as jf
from papp.form_.meanFrm import Meanfrm as mf
from django.forms import BaseForm
import urllib.request
from django.shortcuts import redirect
import numpy as np


#################### 평균 #########################
# ========================= 평균폼 출력
def go_gmean(request):
    mf_= mf

    return render(request, "papp/go_gmean.html", { "title": "평균실습", "message": "빈도수가 상위 10인 데이터중에서 10개의 빈도수 평균보다 높은 데이터만 차트로 출력", "mf_": mf_})  

# ========================= 평균 컬렉션 수집/저장
def go_gmean_save(request):
    print('request.GET.get("id_theme"):' + request.GET.get("id_theme"))
    doNavApi2(pKey = request.GET.get("id_theme"), pColname=request.GET.get("id_theme"))
    print(selCollection())
    return JsonResponse(selCollection(),content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})
     
# ========================= 평균 처리
def go_gmean_proc(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    #json_list = doNavApiXml(request.GET.get('selClass'),request.GET.get('txtColname'))
    print('request.GET.get("id_theme_sel") : ' + request.GET.get('id_theme_sel'))
    json_list = doNavApi(request.GET.get('id_theme_sel'), request.GET.get('id_theme_sel'))
    json_list = Counter(json_list)
    # 10개
    top10 = json_list.most_common(10)
    print('=============')
    print(top10[0][1])
    # 합계
    sume = 0
    # 평균
    means = []

    for t in top10:
        sume = sume + t[1]
        means.append(t[1])

    # 평균구하기
    meanv = np.mean(means)

    # 전송할 배열
    allcon = []
    allcon.append(top10)
    allcon.append(meanv)
    allcon.append(sume)
    
    # 평균
    return JsonResponse(allcon,content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})


#################### 주소 #########################
# 가입 폼
def go_juso(request):
    jf_ = jf()
    print('여기!')
    if request.method == 'POST':
        print('저기!')
        jf_ = jf(request.POST)
        print(jf_.is_valid())
        print(jf_)
        #
        if jf_.is_valid():
            cd = jf_.cleaned_data
            print(cd)
            insertAddrs(cd)
        return redirect('/papp/go_juso/', kwargs={ "title": "가입폼 클래스 스터디 타이틀", "message":"가입폼 스터디 페이징 ㅋㅋ", "jf_": jf_})
    return render(request, "papp/go_juso.html", { "title": "가입폼 클래스 스터디 타이틀", "message": "가입폼 스터디 페이징 ㅋㅋ", "jf_": jf_})

def go_juso_proc(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    #json_list = doNavApiXml(request.GET.get('selClass'),request.GET.get('txtColname'))
    addrs = doJusoApi(request, pKey = request.GET.get("pKey"))
    print(addrs)
    return JsonResponse(addrs,content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})

##################### 로그인 ###############################
def go_login(request):
    lf = LoginFrm()
    return render(request, "papp/go_login.html", { "title": "로그인폼 클래스 스터디 타이틀", "message": "로그인폼 스터디 페이징 ㅋㅋ", "lf": lf})

# 로그인 폼 : 아이디 등록
def go_login_proc(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    #json_list = doNavApiXml(request.GET.get('selClass'),request.GET.get('txtColname'))
    id_userid = request.GET.get("id_userid")
    print(id_userid)
    insertUserid(id_userid)
    
    return JsonResponse(id_userid,content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})

######################### tClass 인터페이스 상속 #############################
# 인터페이스 요청시 실행될 메서드들
def page_inserface_mpi(request):
    vFamily = cmpi.testOtParent() + "," + cmpi.testParentI() + "," + cmpi.testChildMParentI()
    return render(request, "papp/page_inserface_mpi.html", { "title": "다중 상속 클래스 스터디 타이틀", "message": "다중 상속 클래스 스터디 페이징 ㅋㅋ", "vFamily": "부모인터페이스 2개와 자식클래스 1개의 메서드 리턴값 =" + vFamily})

######################### tClass 상속 #############################
# 다중상속 요청시 실행될 메서드들
def page_class_mp(request):
    vFamily = cmp.vChildMParent + cmp.vPrarent + cmp.vPrarentOt
    return render(request, "papp/page_class_mp.html", { "title": "다중 상속 클래스 스터디 타이틀", "message": "다중 상속 클래스 스터디 페이징 ㅋㅋ", "vFamily": "부모클래스 2개와 자식클래스 1개의 변수의 합(vFamily) =" + str(vFamily), "testChildMParent": "자식의 함수리턴 값(testChildMParent()) =" + str(cmp.testChildMParent()), "testParent": "첫번째 부모의 함수리턴 값(testParent()) =" + str(cmp.testParent()), "testOtParent": "두번째 부모의 함수리턴 값(testOtParent()) =" + str(cmp.testOtParent())})

#################### tClass ################################
# 요청 시 실행 될 메서드들
#def page_class(request):
#    resValue = tClassName2.testFunc()
#    return render(request, "papp/page_class.html", {"title":"클래스 스터디 타이틀", "message":"클래스 스터디 페이징 ~~ ", "content1":"(8+9) = " + str(resValue), "content2": "tClassName.vNum = " + str(tClassName.vNum)})


# 4.AJAX요청 doNavApi
def page_move1_proc(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    #json_list = doNavApiXml(request.GET.get('selClass'),request.GET.get('txtColname'))
    json_list = doNavApi(request.GET.get('selClass'),request.GET.get('txtColname'))
    json_list = Counter(json_list)
    return JsonResponse(json_list.most_common(50),content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})

# 폼화면
def page_move1(request):
    return render(request, "papp/page_move1.html", { "title": "페이징타이틀", "message": "페이징 ㅋㅋ", "content": "페이징 컨텐트입니다. "})

#######################################################
def doNMovie2(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    #json_list = doNavApiXml(request.GET.get('selClass'),request.GET.get('txtColname'))
    json_list = doNavMov(request.GET.get('sClass'),request.GET.get('txColname'))
    json_list = Counter(json_list)

    return JsonResponse(json_list.most_common(10),content_type='application/json', 
    safe=False,json_dumps_params={'ensure_ascii':False})

def doNMovie(request):
    return render(request, "papp/movie.html", { "title": "메세지타이틀", 
    "message": "메세지", "content": "메세지 컨텐트입니다. "})

def movie_graph_pie2(request):
    json_list = doNavMov(request.GET.get('sClass'),request.GET.get('txColname'))
    json_list = Counter(json_list) 

    jsonlistmc = json_list.most_common(10)
    return JsonResponse(jsonlistmc,content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})

def movie_graph_pie(request):
    return render(request, 'papp/movie_graph_pie.html')

##################################################
def message_graph_pie2(request):
    json_list = doNavApi(request.GET.get('selClass'),request.GET.get('txColname'))
    json_list = Counter(json_list) 

    jsonlistmc = json_list.most_common(10)
    return JsonResponse(jsonlistmc,content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})

def message_graph_pie(request):
    return render(request, 'papp/message_graph_pie.html')

# 2.문장출력
def doMessage2(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    #json_list = doNavApiXml(request.GET.get('selClass'),request.GET.get('txtColname'))
    json_list = doNavApi(request.GET.get('selClass'),request.GET.get('txtColname'))
    json_list = Counter(json_list)

    return JsonResponse(json_list.most_common(10),content_type='application/json', 
    safe=False,json_dumps_params={'ensure_ascii':False})

def doMessage(request):
    return render(request, "papp/message.html", { "title": "메세지타이틀", 
    "message": "메세지", "content": "메세지 컨텐트입니다. "})

def doDate(request):
    # 문장출력
    return render( request, "papp/date.html", 
    {"title": "Date 타이틀", "date": datetime.now(tz=None), "content": "Date 컨텐트입니다."}
    )

def doTime(request):
    # 문장출력
    return render( request, "papp/time.html", 
    {"title": "Time 타이틀", "date": datetime.now(tz=None), "content": "Time 컨텐트입니다."}
    )

# 1. 요청시 방가! 장고 텍스트를 리턴
def rtnBangga(request):
    return HttpResponse("방가? 장고")
   
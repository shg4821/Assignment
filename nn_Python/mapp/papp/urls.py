"""papp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from papp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.doMessage, name="message"),

    # 페이지 이동1
    # 폼화면
    path("papp/page_move1/", views.page_move1, name="page_move1"),
    # AJAX 네이버 요청
    path("papp/page_move1_proc/", views.page_move1_proc, name="page_move1_proc"),

    # 빈도수 검색기 폼화면
    path("papp/message/", views.doMessage, name="message"),
    # ajax가 리퀘스트 URL과 함수
    path("papp/message2/", views.doMessage2, name="message2"),

    path("papp/movie/", views.doNMovie, name="movie"),
    path("papp/movie2/", views.doNMovie2, name="movie2"),

    path("papp/date/", views.doDate, name="date"),
    path("papp/time/", views.doTime, name="time"),

    path("papp/message_graph_pie/",
         views.message_graph_pie, name="message_graph_pie"),
    path("papp/message_graph_pie2/",
         views.message_graph_pie2, name="message_graph_pie2"),

    path("papp/movie_graph_pie/", views.movie_graph_pie, name="movie_graph_pie"),
    path("papp/movie_graph_pie2/", views.movie_graph_pie2, name="movie_graph_pie2"),

    # 클래스
    # 폼화면
    # path("papp/page_class/", views.page_class, name="page_class"),
    # AJAX  요청
    # path("papp/page_class_proc/", views.page_class_proc, name="page_class_proc"),

    # 다중상속폼화면
    path("papp/page_class_mp/", views.page_class_mp, name="page_class_mp"),
    # 인터페이스폼화면
    path("papp/page_inserface_mpi/",
         views.page_inserface_mpi, name="page_inserface_mpi"),

    # 로그인
    path("papp/go_login/", views.go_login, name="go_login"),
    path("papp/go_login_proc/", views.go_login_proc, name="go_login_proc"),

    # 주소
    # 폼
    path("papp/go_juso/", views.go_juso, name="go_juso"),
    # 에이작스
    path("papp/go_juso_proc/", views.go_juso_proc, name="go_juso_proc"),

    # 평균
    # 폼
    path("papp/go_gmean/", views.go_gmean, name="go_gmean"),
    # 수집/저장
    path("papp/go_gmean_save/", views.go_gmean_save, name="go_gmean_save"),
    # 처리
    path("papp/go_gmean_proc/", views.go_gmean_proc, name="go_gmean_proc"),
]

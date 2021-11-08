from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main, name='main'),
    path('host/', views.host, name='host'),
    path('regist/', views.regist, name='regist'),
    path('lists/', views.lists, name='lists'),
    path('<int:cafe_id>/', views.detail, name='detail'),
    path('image/', views.image, name='image'),
    path('rcmd/', views.rcmd, name='rcmd'),
    path('create/', views.create, name='create'),
    path('<int:cafe_id>/review', views.review, name='review'),
    path('mypage/', views.mypage, name='mypage'),
    path('like/<int:cafe_id>/',views.like, name='like'),
    path('mark/<int:cafe_id>/',views.mark, name="mark"),
    path('mypage/markedcafe/', views.marked_cafe, name='markedcafe'),
    path('mypage/mysetting/', views.mysetting, name='mysetting'),
    path('mypage/version/', views.version, name='version'),
]


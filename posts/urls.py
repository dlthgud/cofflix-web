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
]


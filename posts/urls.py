from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main, name='main'),
    path('host/join', views.join, name="join"),
    path('host/address', views.host, name='host'),
    path('host/theme', views.theme, name='theme'),
]
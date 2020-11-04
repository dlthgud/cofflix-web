from django.urls import path

from . import views

urlpatterns = [
    # test
    path('', views.index, name='index'),

]
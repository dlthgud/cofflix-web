from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'posts/index.html')

def theme(request):
    return render(request, 'posts/theme.html')
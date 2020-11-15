from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'posts/main.html')

def join(request):
    return render(request, 'posts/host/join.html')

def host(request):
    return render(request, 'posts/host/host.html')

def theme(request):
    return render(request, 'posts/host/theme.html')

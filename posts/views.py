from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'posts/main.html')

def host(request):
    return render(request, 'posts/host.html')

def theme(request):
    return render(request, 'posts/theme.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Cafe, Tag, Image
import json
import datetime


def main(request):
    return render(request, 'posts/main.html')


def host(request):
    return render(request, 'posts/host.html')


def regist(request):
    name = request.POST['name']
    tel = request.POST['tel']
    address = request.POST['address'] + ' ' + request.POST['detailAddress']
    ot = datetime.time(hour=int(request.POST['openTime']))
    ct = datetime.time(hour=int(request.POST['closeTime']))
    body = request.POST['body']
    cafe = Cafe(name=name, memo=body, address=address, open_time=ot, close_time=ct, tel=tel)
    cafe.save()

    if 'image[]' in request.FILES:
        images = request.FILES.getlist('image[]')
        for image in images:
            img = Image(cafe=cafe, image=image)
            img.save()

    tags = request.POST['tags'].split(",")
    for tag in tags:
        taged = Tag.objects.filter(name=tag).first()
        cafe.tags.add(taged.id)

    images = request.FILES.getlist('image')
    for image in images:
        item = Image(cafe=cafe, image=image)
        item.save()

    return redirect('posts:main')


def lists(request):
    keywords = []
    # print(request.GET)
    if 'keywords[]' in request.GET.keys():
        keywords = request.GET.getlist('keywords[]')

        keyword = keywords.pop()
        cafes = Cafe.objects.filter(tags__name=keyword)

        for keyword in keywords:
            cafes = cafes.filter(tags__name=keyword)
    else:
        cafes = Cafe.objects.all()

    if request.is_ajax():
        cafes = serialize('json', cafes)
        cafes = json.loads(cafes)
        cafes = list(map(lambda cafe: cafe["fields"], cafes))
        return HttpResponse(json.dumps({"cafes": cafes}), content_type="application/json")

    return render(request, 'posts/lists.html', {"cafes": cafes})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from django.db.models import Count
from .models import Cafe, Tag, Image
import json
import datetime


def main(request):
    total = Cafe.objects.annotate(num_tags=Count('tags')).filter(num_tags__gt=1).count()
    cafes = Cafe.objects.annotate(num_tags=Count('tags')).filter(num_tags__gt=1).order_by('-num_tags', 'id')[:4]
    context = {
        'total': total,
        'cafes': cafes,
    }
    return render(request, 'posts/main.html', context)


def rcmd(request):
    num = int(request.GET['num']) - 1
    cafe = Cafe.objects.annotate(num_tags=Count('tags')).filter(num_tags__gt=1).order_by('-num_tags', 'id')[num: num+1]
    if cafe:
        cafe = serialize('json', cafe)
        cafe = json.loads(cafe)
        cafe = list(map(lambda cafe: {'id': cafe["pk"], **cafe["fields"]}, cafe))
        context = {
            'result': True,
            'cafe': cafe,
        }
    else:
        context = { 'result': False }
    return HttpResponse(json.dumps(context), content_type="application/json")


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
    if len(tags) > 0 and tags[0]:
        for tag in tags:
            taged = Tag.objects.filter(name=tag).first()
            cafe.tags.add(taged.id)

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
        cafes = list(map(lambda cafe: {'id': cafe["pk"], **cafe["fields"]}, cafes))
        return HttpResponse(json.dumps({"cafes": cafes}), content_type="application/json")

    return render(request, 'posts/lists.html', {"cafes": cafes})


def image(request):
    cafe = request.GET['cafe']
    image = Image.objects.filter(cafe=cafe).first()
    if image:
        image = image.image.url
    return HttpResponse(json.dumps({"image": image}), content_type="application/json")

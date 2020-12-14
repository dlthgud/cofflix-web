from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from django.db.models import Count
from .models import Cafe, Tag, Image
import json
import requests
import datetime
 
# 카카오 API 맵 
def getLatLng(address):
    result = ""
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = 'd975e180da8e3f1265e42a90c8ca1875'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
 
    r = requests.get(url, headers=header)
 
    if r.status_code == 200:
        result_address = r.json()["documents"][0]["address"]
        
        result = result_address["y"], result_address["x"]
    else:
        result = "ERROR[" + str(r.status_code) + "]"
    
    return result
 
 
def getKakaoMapHtml(address_latlng):
    javascript_key = "45522189c1ececf745d0f4c8c482b82e"
 
    result = ""
    result = result + "<div id='map' style='width:300px;height:200px;display:inline-block;'></div>" + "\n"
    result = result + "<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + javascript_key + "'></script>" + "\n"
    result = result + "<script>" + "\n"
    result = result + "    var container = document.getElementById('map'); " + "\n"
    result = result + "    var options = {" + "\n"
    result = result + "           center: new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ")," + "\n"
    result = result + "           level: 3" + "\n"
    result = result + "    }; " + "\n"
    result = result + "    var map = new kakao.maps.Map(container, options); " + "\n"
    
    # 검색한 좌표의 마커 생성을 위해 추가
    result = result + "    var markerPosition  = new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ");  " + "\n"
    result = result + "    var marker = new kakao.maps.Marker({position: markerPosition}); " + "\n"
    result = result + "    marker.setMap(map); " + "\n"
 
    result = result + "</script>" + "\n"
    
    return result
 
# main()
if __name__ == "__main__":
    address = "서울 강남구 선릉로 669"
    
    # 카카오 REST API로 좌표 구하기
    address_latlng = getLatLng(address)
 
    # 좌표로 지도 첨부 HTML 생성
    if str(address_latlng).find("ERROR") < 0:
        map_html = getKakaoMapHtml(address_latlng)
        
        print(map_html)
    else:
        print("[ERROR]getLatLng")




#-------------------------카카오맵--------------------
 

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

def detail(request):
    return render(request, 'posts/detail.html')


def image(request):
    cafe = request.GET['cafe']
    image = Image.objects.filter(cafe=cafe).first()
    if image:
        image = image.image.url
    return HttpResponse(json.dumps({"image": image}), content_type="application/json")

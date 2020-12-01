from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
 
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
    return render(request, 'posts/main.html')


def host(request):
    return render(request, 'posts/host.html')


def theme(request):
    return render(request, 'posts/theme.html')


def lists(request):
    content = {
        "cafes": [
            {
                "name": "스타벅스",
                "desc": "서교동",
                "tags": ["테라스", "주차가능", "애완동물동반", "1인카페"],
                "img": "https://dtd31o1ybbmk8.cloudfront.net/photos/ba1b1c1b8c7f1c3475980282a46e4fa5/thumb.jpg",
            },
            {
                "name": "카페베네",
                "desc": "합정동",
                "tags": ["테라스", "주차가능", "애완동물동반", "1인카페"],
                "img": "https://ojsfile.ohmynews.com/STD_IMG_FILE/2012/1011/IE001499462_STD.JPG",
            },
            {
                "name": "투썸플레이스",
                "desc": "망원동",
                "tags": ["테라스", "주차가능", "애완동물동반", "1인카페", "소파가편한", "산미가 나는 원두"],
                "img": "https://news.kbs.co.kr/data/news/2019/03/20/4161682_XOR.jpg",
            },
            {
                "name": "이디야",
                "desc": "연남동",
                "tags": ["주차가능", "애완동물동반", "1인카페"],
                "img": "https://ediya.com/C/images/ediya/m_con_img02.gif",
            },
            {
                "name": "엔제리너스",
                "desc": "연희동",
                "tags": ["애완동물동반", "소파가편한", "산미가 나는 원두", "디카페인"],
                "img": "https://image.chosun.com/sitedata/image/202001/03/2020010300862_0.png",
            }
        ]
    }

    keywords = []
    # print(request.GET)
    if 'keywords[]' in request.GET.keys():
        keywords = request.GET.getlist('keywords[]')
        for keyword in keywords:
            content["cafes"] = list(filter(lambda x: keyword in x["tags"], content["cafes"]))

    if request.is_ajax():
        return HttpResponse(json.dumps(content), content_type="application/json")

    return render(request, 'posts/lists.html', content)


def detail(request):
    return render(request, 'posts/detail.html')

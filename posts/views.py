from django.shortcuts import render
from django.http import HttpResponse
import json


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
    print(request.GET)
    if 'keywords[]' in request.GET.keys():
        keywords = request.GET.getlist('keywords[]')
        for keyword in keywords:
            content["cafes"] = list(filter(lambda x: keyword in x["tags"], content["cafes"]))

    if request.is_ajax():
        return HttpResponse(json.dumps(content), content_type="application/json")

    return render(request, 'posts/lists.html', content)

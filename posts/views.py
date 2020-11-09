from django.shortcuts import render
from django.http import HttpResponse
import json


def main(request):
    content = {
        "cafes": [
            {
                "name": "스타벅스",
                "desc": "서교동",
                "tags": ["테라스", "주차가능", "애완동물동반", "1인카페"],
            },
            {
                "name": "카페베네",
                "desc": "합정동",
                "tags": ["테라스", "주차가능", "애완동물동반", "1인카페"],
            },
            {
                "name": "투썸플레이스",
                "desc": "망원동",
                "tags": ["테라스", "주차가능", "애완동물동반", "1인카페", "소파가편한", "산미가 나는 원두"],
            },
            {
                "name": "이디야",
                "desc": "연남동",
                "tags": ["주차가능", "애완동물동반", "1인카페"],
            },
            {
                "name": "엔제리너스",
                "desc": "연희동",
                "tags": ["애완동물동반", "소파가편한", "산미가 나는 원두", "디카페인"],
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

    return render(request, 'posts/main.html', content)


def host(request):
    return render(request, 'posts/host.html')


def theme(request):
    return render(request, 'posts/theme.html')

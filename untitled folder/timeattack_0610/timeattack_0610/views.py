from django.shortcuts import render
from django.http import HttpResponse


def base_response(request):
    return HttpResponse("안녕하세요 ! 장고페이지 첫 띄우기!")


def first_view(request):
    return render(request, "detail.html")

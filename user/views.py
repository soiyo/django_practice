from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하는 함수 -sign_up_view와 연결됨
from .models import UserModel
from django.http import HttpResponse
from django.contrib import auth  # 사용자 auth 기능 - sign_in_view와 연결됨

# Create your views here.
def sign_up_view(request):
    if request.method == "GET":
        return render(request, "user/signup.html")
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get("password2", None)
        bio = request.POST.get("bio", None)

        if password != password2:
            return render(request, "user/signup.html")
        else:
            # 아이디 중복 체크
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, "user/signup.html")
            else:
                UserModel.objects.create_user(
                    username=username, password=password, bio=bio
                )
                return redirect("/sign-in")


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        me = auth.authenticate(
            request, username=username, password=password
        )  # 사용자 불러오기
        if me is not None:
            auth.login(request, me)
            return redirect("/")  # 로그인 성공시
        else:
            return redirect("/sign-in")
    if request.method == "GET":
        return render(request, "user/signin.html")

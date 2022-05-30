from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하는 함수 -sign_up_view와 연결됨
from .models import UserModel
from django.http import HttpResponse
from django.contrib import auth  # 사용자 auth 기능 - sign_in_view와 연결됨
from django.contrib.auth.decorators import login_required


@login_required  # 로그인하지 않으면 접근 불가능하게 만드는 기능
def logout(request):
    auth.logout(request)  # 인증되어있는 정보 없애기
    return redirect("/")


# Create your views here.
def sign_up_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated  # 로그인 여부만 검증해주는 기능
        if user:
            return redirect("/")
        else:
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
        user = request.user.is_authenticated
        if user:
            return redirect("/")
        else:
            return render(request, "user/signin.html")

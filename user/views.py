import re
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
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")
        bio = request.POST.get("bio", "")

        if password != password2:
            return render(request, "user/signup.html", {"error": "패스워드를 확인해 주세요!"})
        else:
            if username == "" or password == "":
                return render(
                    request, "user/signup.html", {"error": "사용자 이름과 패스워드는 필수값입니다."}
                )
            # 아이디 중복 체크
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, "user/signup.html", {"error": "사용자가 존재합니다."})
            else:
                UserModel.objects.create_user(
                    username=username, password=password, bio=bio
                )
                return redirect("/sign-in")


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        me = auth.authenticate(
            request, username=username, password=password
        )  # 사용자 불러오기
        if me is not None:
            auth.login(request, me)
            return redirect("/")  # 로그인 성공시
        else:
            return render(
                request, "user/signin.html", {"error": "유저이름 혹은 패스워드를 확인해주세요."}
            )
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect("/")
        else:
            return render(request, "user/signin.html")


@login_required
def user_view(request):
    if request.method == "GET":
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, "user/user_list.html", {"user_list": user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():  # user.followee.all 해당 사용자를 팔로워 하는 사람들을 불러옵
        # user.follow.all()는 해당 사용자가 팔로우 하는 사람들을 불러옵니다.
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect("/user")

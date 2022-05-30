from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인 되어있는지) 검사해주는 기능
    if user:
        return redirect("/tweet")
    else:
        return redirect("/sign-in")


def tweet(request):
    if request.method == "GET":
        return render(request, "tweet/home.html")

from .models import TweetComment, TweetModel  # 글쓰기모델 : 가장 윗부분에 적어주기
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def delete_tweet(request, id):  # 이 id는 게시글 고유의 id로써 게시글을 구분 하는 데에 사용 할 변수임
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect("/tweet")


@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by("-created_at")
    return render(
        request,
        "tweet/tweet_detail.html",
        {"tweet": my_tweet, "comment": tweet_comment},
    )


@login_required
def write_comment(request, id):
    if request.method == "POST":
        comment = request.POST.get("comment", "")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect("/tweet/" + str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect("/tweet/" + str(current_tweet))


# Create your views here.
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인 되어있는지) 검사해주는 기능
    if user:
        return redirect("/tweet")
    else:
        return redirect("/sign-in")


def tweet(request):
    if request.method == "GET":
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인한 사용자라면
            all_tweet = TweetModel.objects.all().order_by("-created_at")
            # TweetModel을 created_at의 역순으로 불러오는 코드
            return render(request, "tweet/home.html", {"tweet": all_tweet})
            # tweet/home.html을 화면에 띄우면서 {'tweet':all_tweet} 라는 데이터를 화면에 전달한다
        else:
            return redirect("/sign-in")
    elif request.method == "POST":
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # 글쓰기 모델 가져오기
        my_tweet.author = user  # 모델에 사용자 저장
        my_tweet.content = request.POST.get(
            "my-content", ""
        )  # 모델에 글 저장, html에서 id와 name이 'my-content'였음
        my_tweet.save()
        return redirect("/tweet")

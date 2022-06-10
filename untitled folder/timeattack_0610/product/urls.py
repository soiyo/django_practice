from django.urls import path
from . import views

urlpatterns = [
    path(
        "detail/", views.home, name="home"
    ),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
]

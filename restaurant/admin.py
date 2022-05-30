from django.contrib import admin
from .models import MyTopping, MyPizza

# Register your models here.
admin.site.register(MyPizza)
admin.site.register(MyTopping)

# admin.py에서 데이터베이스 모델을 추가 해 주고 from .models import MyTopping, MyPizza 우리가 사용 할 어드민 페이지에 추가 admin.site.register(MyPizza), admin.site.register(MyTopping) 해 주었습니다.

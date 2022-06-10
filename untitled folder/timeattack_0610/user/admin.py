from django.contrib import admin

# Register your models here.
from .models import User

#  models.py에서 클래스를 가져옴
admin.site.register(User)

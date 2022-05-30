from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    bio = models.TextField(max_length=256, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followee")
    # 장고에서 사용할 유저모델은 바로 settings.py에 AUTH_USER_MODEL로 선언이 되어있음

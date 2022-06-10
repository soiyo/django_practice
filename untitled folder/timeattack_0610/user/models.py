from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.TextField(max_length=256, blank=True)
    password = models.TextField(max_length=256, blank=True)

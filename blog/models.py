# blog 앱 파일이 통째로 중간에 날아갔다 ... (templates/blog 를 옮기다가 blog앱에 덮어쓰기가 된 사실을 나중에 알았다)
# 그래서 models.py는 완성되지 않았지만 db 만 있는 이상한(?) 상태 ..?
from django.db import models


class CategoryModel(models.Model):
     class Meta:
        db_table = "category"
    category = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)

class Article(models.Model):
    class Meta:
        db_table = "article"

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
from genericpath import exists
from django.db import models
from django.conf import settings

# Create your models here.
class OrderStatus(models.Model):
    class Meta:
        db_table = "my_order"

    order_complete = models.TextField(max_length=256, blank=True)
    money_complete = models.TextField(max_length=256, blank=True)
    order_cancel = models.TextField(max_length=256, blank=True)
    send_start = models.DateTimeField()
    send_complete = models.DateTimeField()


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    category = models.TextField(max_length=256, blank=True)


# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "product"

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.TextField(max_length=256, blank=True)
    product_img = models.TextField(max_length=256, blank=True)
    product_desc = models.TextField(max_length=256, blank=True)
    product_price = models.TextField(max_length=256, blank=True)
    product_stock = models.TextField(max_length=256, blank=True)


# Create your models here.
class ProductOrder(models.Model):
    class Meta:
        db_table = "productorder"

    order_complete = models.ForeignKey(Category, on_delete=models.CASCADE)
    order_count = models.TextField(max_length=256, blank=True)


# Create your models here.
class UserOrder(models.Model):
    class Meta:
        db_table = "userorder"

    order_complete = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.TextField(max_length=256, blank=True)
    order_time = models.DateTimeField()
    order_all_price = models.TextField(max_length=256, blank=True)
    discount_rate = models.TextField(max_length=256, blank=True)
    total_price = models.TextField(max_length=256, blank=True)
    exists_order = models.TextField(max_length=256, blank=True)

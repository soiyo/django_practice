from django.urls import path
from . import views

urlpatterns = [path("drink/", views.drink_view, name="drink")]

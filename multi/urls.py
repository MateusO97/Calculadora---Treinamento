from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.multi_multiplication, name='multi_multiplication'),
    path('multi/see_all', views.see_all, name='see_all'),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.multi_multiplication, name='multi_multiplication'),
]
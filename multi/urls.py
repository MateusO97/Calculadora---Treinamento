from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('multi/multi_multiplication', views.multi_multiplication, name='multi_multiplication'),
    path('multi/see_all', views.see_all, name='see_all'),
    path('edit/<int:id>', views.edit_operation, name='edit_operation'),
]
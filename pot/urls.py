from django.urls import path,include
from . import views

urlpatterns = [
    path('operation_screen/', views.operation_screen),
]

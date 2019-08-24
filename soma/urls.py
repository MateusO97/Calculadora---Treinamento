from django.urls import path
from . import views

urlpatterns = [
    path('soma',views.calculo, name='calculo'),
]

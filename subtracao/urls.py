from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_de_operacao, name='tela_de_operacao'),
]

from django.shortcuts import render
from .forms import SubForm

def tela_de_operacao(request):
    return render(request, 'subtracao/tela_de_operacao.html', {})

def sub_new(request):
    form = SubForm()
    return render(request, 'subtracao/tela_de_operacao.html',  {'form': form})

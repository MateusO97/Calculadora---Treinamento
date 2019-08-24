from django.shortcuts import render

def tela_de_operacao(request):
    return render(request, 'subtracao/tela_de_operacao.html', {})

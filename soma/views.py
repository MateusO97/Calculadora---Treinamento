from django.shortcuts import render

# Create your views here.
def calculo(request):
    return render(request, 'soma/calculo.html', {})

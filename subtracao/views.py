from django.shortcuts import render, redirect
from .forms import SubForm
from .models import Operacao
from django.utils import timezone

def tela_de_operacao(request):
    operacoes = Operacao.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            operacao = form.save(commit=False)
            cd = form.cleaned_data
            input1 = cd['number1']
            input2 = cd['number2']
            operacao.result = input1 - input2
            operacao.published_date = timezone.now()
            operacao.save()
            return redirect('tela_de_operacao')
    else:
        form = SubForm()
    return render(request, 'subtracao/tela_de_operacao.html', {'form': form, 'operacoes': operacoes})


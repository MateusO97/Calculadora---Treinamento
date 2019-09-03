from django.shortcuts import render
from .forms import PotForm

# Create your views here.
def operation_screen(request):
    form = PotForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.potentiation()
            obj.save()
    return render(request, 'teste.html', {'form': form})

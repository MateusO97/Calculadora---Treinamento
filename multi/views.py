from django.shortcuts import render, redirect, get_object_or_404
from .forms import MultiForm
from django.http import HttpResponse
from multi.models import Multi

# Create your views here.
def home(request):
    return render(request, 'multi/Home.html', {})

def  multi_multiplication(request):
    form = MultiForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.res = form.multi()
            post.save()
            return render(request, 'multi/Multi.html', {'form': form})
        else:
            print(form.errors)
            return render(request, 'multi/Multi.html', {'form': form})
    else:
        return render(request, 'multi/Multi.html', {'form': form})

def see_all(request):
    operations = Multi.objects.all()
    return render(request, 'multi/SeeAll.html', {'operations': operations})

def edit_operation(request, id):
    operation = get_object_or_404(Multi, pk=id) #Pega objeto por objeto da model passada
    form = MultiForm(instance=operation) #Pega o formulário com os dados do objeto passado

    if(request.method == 'POST'):
        form = MultiForm(request.POST, instance=operation)

        if(form.is_valid()):
            form.save()
            return redirect('/')
        else:
            return render(request, 'multi/EditOperation.html', {'form': form, 'operation': operation})
    else:
        return render(request, 'multi/EditOperation.html', {'form': form, 'operation': operation})
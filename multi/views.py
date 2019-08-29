from django.shortcuts import render, redirect
from .forms import MultiForm
from django.http import HttpResponse

# Create your views here.
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
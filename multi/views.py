from django.shortcuts import render

# Create your views here.
def multi_number(request):
    return render(request, 'multi/Multi.html', {})
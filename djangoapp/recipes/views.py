from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
    return render(request, 'recipes/home.html')

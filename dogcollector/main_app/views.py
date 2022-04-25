from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Dog


def home(request):
    return HttpResponse('<h1>hello world</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dog/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dog/detail.html', {'dog': dog})
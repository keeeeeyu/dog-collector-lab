from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Woody', 'Goldendoodle', 'two brown ears', 1),
    Dog('Benji', 'Shih tzu', 'Ponytail hair', 1),
    Dog('Liah', 'Aussie', 'blue eyes', 0)
]




def home(request):
    return HttpResponse('<h1>hello world</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dog/index.html', {'dogs': dogs})
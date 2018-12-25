from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def food(request):
    return render(request, 'my_app/food.html')

def new_food(request):
    return render(request, 'my_app/new_food.html')         

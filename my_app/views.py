from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import View
from my_app.forms import WeightForm

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

class EnterWeight(View):

    def get(self, request):
        form = WeightForm()
        c = {'form': form}
        return render(request, 'my_app/form_weight.html', c)

    def post(self, request):
        form = WeightForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            form = WeightForm(instance=form)
        return redirect('/index')

def food(request):
    return render(request, 'my_app/food.html')

def new_food(request):
    return render(request, 'my_app/new_food.html')

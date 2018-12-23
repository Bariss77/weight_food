from django.shortcuts import render

# Create your views here.
def start_list(request):
    return render(request, 'my_app/start_list.html', {})

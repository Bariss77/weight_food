from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from my_app.models import Weight
from my_app.views import EnterWeight


urlpatterns = [
    path('', ListView.as_view(queryset=Weight.objects.all().order_by("-date"), template_name="my_app/index.html")),
    path('index/', ListView.as_view(queryset=Weight.objects.all().order_by("-date"), template_name="my_app/index.html")),

    path('form_weight/', EnterWeight.as_view(), name='form'),

    path('food/', views.food, name='food'),
    path('new_food/', views.new_food, name='new_food'),
]

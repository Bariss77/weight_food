from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('food/', views.food, name='food'),
    path('new_food/', views.new_food, name='new_food'),
]

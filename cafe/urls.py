from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cafes/', views.cafes, name='cafes'),
    path('add/', views.add, name='add'),
]
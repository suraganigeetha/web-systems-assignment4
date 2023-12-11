# calculator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tip_calculator, name='tip_calculator'),
]

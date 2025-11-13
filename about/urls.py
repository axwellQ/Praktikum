from django.urls import path
from django import views

urlpatterns = [
    path('', views.description, name='about'),  # Путь about/ -> функция description
]
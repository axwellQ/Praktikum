from django.urls import path
#from . import views

urlpatterns = [
    path('', views.description, name='about'),  # Путь about/ -> функция description
]
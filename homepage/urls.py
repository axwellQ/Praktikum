from django.urls import path
from . import views  # Импорт view-функций из текущего приложения

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница использует функцию index
]
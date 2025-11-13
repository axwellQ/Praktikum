from django.contrib import admin
from django.urls import path, include  # Добавлен импорт include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Подключение маршрутов из приложения homepage
]
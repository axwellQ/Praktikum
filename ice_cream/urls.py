from django.urls import path
# from . import views

urlpatterns = [
    path('', views.ice_cream_list, name='ice_cream_list'),  # Обработка адреса ice_cream/
    path('<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),  # Обработка адресов вида ice_cream/1/, ice_cream/2/ и т.д.
]
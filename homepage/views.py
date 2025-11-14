from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница') # Возвращает текст для главной страницы
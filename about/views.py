from django.http import HttpResponse


def description(request):
    return HttpResponse('Описание проекта') # Возвращает текст для страницы about/
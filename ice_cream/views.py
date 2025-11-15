from django.http import HttpResponse

# Константа не нужна, так как в задании не требуется выводить символ мороженого
# ICE_CREAM = chr(127846)


def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')


def ice_cream_list(request):
    return HttpResponse('Каталог мороженого') # Возвращает текст для списка мороженого
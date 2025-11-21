from django.shortcuts import render


def description(request):
    return render(request, 'about/description.html')


def index(request):
    return render(request, 'homepage/index.html')


def ice_cream_list(request):
    return render(request, 'ice_cream/list.html')
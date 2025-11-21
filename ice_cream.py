from django.shortcuts import render


def ice_cream_detail(request, pk):
    return render(request, 'ice_cream/detail.html')


def ice_cream_list(request):
    return render(request, 'ice_cream/list.html')
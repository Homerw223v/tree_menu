from django.shortcuts import render


def menu(request, *args):
    return render(request, 'menu/home.html', context={'slug': request.path[1:]})

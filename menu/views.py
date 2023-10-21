from django.shortcuts import render


def menu(request, slug=None, *args):
    return render(request,
                  'menu/home.html',
                  context={'slug': request.path[1:]})

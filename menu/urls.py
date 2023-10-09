from django.urls import path, re_path

from .views import menu

urlpatterns = [
    re_path(r'|(http://[a-zA-Z0-9_\./]?:pk+)|', menu, name='menu'),
]

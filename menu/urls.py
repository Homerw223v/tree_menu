from django.urls import path

from .views import menu

app_name = 'tree_menu'

urlpatterns = [
    path('', menu, name='start_page'),
    path('<str:slug>', menu, name='menu')
]

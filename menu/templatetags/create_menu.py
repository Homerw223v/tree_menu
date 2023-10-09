from django import template
from django.db.models import QuerySet

from ..models import Menu

register = template.Library()
base_url = str()
current_url = str()


def check_set_url() -> None:
    """Create new current url
    :rtype: None"""
    global current_url, base_url
    url_now_len: int = len(current_url.split('-'))
    base_url_len: int = len(base_url.split('-'))
    if url_now_len == base_url_len:
        current_url = '-'.join((base_url.split('-')[:url_now_len]))
    elif url_now_len < base_url_len:
        current_url = '-'.join((base_url.split('-')[:url_now_len + 1]))
    else:
        current_url = None


@register.inclusion_tag('menu/menu.html')
def children(query: list) -> dict:
    """Create children menu if need
    :param query:
    :type query: list
    :rtype: dict
    """
    global base_url, current_url
    menu: list = list()
    left: list = list()
    for table in query:
        if table.parent.url == current_url:
            menu.append(table)
        else:
            left.append(table)
    check_set_url()
    return {'left': left, 'main_menu': menu, 'menu_url': current_url, 'base': base_url}


@register.inclusion_tag('menu/menu.html')
def draw_menu(url: str) -> dict:
    """Create base menu
    :param url:
    :type url: str
    :return:
    """
    global current_url, base_url
    base_url = url
    current_url = None if base_url == '' else base_url.split('-')[0]
    menu: QuerySet = Menu.objects.select_related('parent').order_by('name')
    main_menu: list = []
    left: list = []
    if menu:
        for table in menu:
            if table.parent is None:
                main_menu.append(table)
            else:
                left.append(table)
        return {'main_menu': main_menu, 'left': left, 'base': base_url, 'menu_url': current_url}
    return dict()

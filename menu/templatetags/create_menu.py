from django import template
from django.db.models import Q
from ..models import Menu

register = template.Library()


def set_current_url(current_url: str, base_url: str) -> str | None:
    """Create new current url
    :param current_url:
    :type current_url: str
    :param base_url:
    :type base_url: str
    :rtype: dict | None
    """
    url_now_len = len(current_url.split('-'))
    base_url_len = len(base_url.split('-'))
    if url_now_len == base_url_len:
        return '-'.join(base_url.split('-')[:url_now_len])
    elif url_now_len < base_url_len:
        return '-'.join(base_url.split('-')[:url_now_len + 1])
    else:
        return None


def get_urls(url: str) -> list:
    """Return urls list that will be used in SQL query
    :param url:
    :type url: str
    :rtype: list"""
    url_list = []
    urls = url.split('-')
    for i in range(len(urls)):
        url_list.append('-'.join(urls[:i + 1]))
    return url_list


@register.inclusion_tag('menu/menu.html')
def children(query: list, current_url: str, base_url: str) -> dict:
    """Create children menu, if needed
    :param query:
    :type query: list
    :param current_url:
    :type current_url: str
    :param base_url:
    :type base_url: str
    :rtype: dict
    """
    menu = []
    left = []
    for table in query:
        if table.parent.url == current_url:
            menu.append(table)
        else:
            left.append(table)
    current_url = set_current_url(current_url, base_url)
    return {'left': left, 'main_menu': menu, 'menu_url': current_url, 'base': base_url}


@register.inclusion_tag('menu/menu.html')
def draw_menu(url: str) -> dict:
    """Create base menu
    :param url:
    :type url: str
    :rtype: dict
    """
    base_url = url
    current_url = '' if base_url == '' else base_url.split('-')[0]
    menu = Menu.objects.filter(Q(parent=None) | Q(parent__url__in=get_urls(base_url))).select_related(
        'parent').order_by('name')
    main_menu = []
    left = []
    if menu:
        for table in menu:
            if table.parent is None:
                main_menu.append(table)
            else:
                left.append(table)
        return {'main_menu': main_menu, 'left': left, 'base': base_url, 'menu_url': current_url}
    return {}

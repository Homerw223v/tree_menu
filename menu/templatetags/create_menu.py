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
    :rtype: str | None
    """
    url_now_len = len(current_url.split('-'))
    base_url_len = len(base_url.split('-'))
    if url_now_len == base_url_len:
        return '-'.join(base_url.split('-')[:url_now_len])
    elif url_now_len < base_url_len:
        return '-'.join(base_url.split('-')[:url_now_len + 1])
    return None


def get_urls(url: str) -> list:
    """Return urls list that will be used in SQL query
    :param url:
    :type url: str
    :rtype: list"""
    urls = url.split('-')
    return ['-'.join(urls[:i + 1]) for i in range(len(urls))]


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
    menu = Menu.objects.filter(Q(parent=None) | Q(parent__url__in=get_urls(url))).select_related(
        'parent').order_by('name')
    main_menu = []
    left = []
    if menu:
        for table in menu:
            if table.parent is None:
                main_menu.append(table)
            else:
                left.append(table)
    return {'main_menu': main_menu, 'left': left, 'base': url, 'menu_url': url.split('-')[0]}

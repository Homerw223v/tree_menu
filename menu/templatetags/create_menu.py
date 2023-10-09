from django import template

from ..models import Menu

register = template.Library()


def check_set_url(current_url: str, base_url: str) -> str | None:
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


@register.inclusion_tag('menu/menu.html')
def children(query: list, current_url: str, base_url: str) -> dict:
    """Create children menu if need
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
    current_url = check_set_url(current_url, base_url)
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
    menu = Menu.objects.select_related('parent').order_by('name')
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

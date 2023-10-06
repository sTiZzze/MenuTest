from django import template
from django.http import request
from django.urls import resolve, Resolver404
from src.menu.models import MenuItem


register = template.Library()


@register.simple_tag
def draw_menu(menu_name, request):
    try:
        menu = MenuItem.objects.get(title=menu_name)
        current_url = resolve(request.path_info).url_name
        return render_menu(menu, current_url)
    except MenuItem.DoesNotExist:
        return ""


def render_menu(menu_item, current_url):
    html = "<ul>"
    for item in MenuItem.objects.filter(parent=menu_item):
        is_active = item.named_url == current_url
        css_class = "active" if is_active else ""
        html += f"<li class='{css_class}'><a href='{item.url}'>{item.title}</a>"
        children = MenuItem.objects.filter(parent=item)
        if children:
            html += "<ul>"
            for child in children:
                html += render_menu(child, current_url)
            html += "</ul>"
        html += "</li>"
    html += "</ul>"
    return html
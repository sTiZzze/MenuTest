from django.shortcuts import render, HttpResponse
from src.menu.models import MenuItem


def my_view(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items, 'request': request}
    return render(request, 'my_template.html', context)

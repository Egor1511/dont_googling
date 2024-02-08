from django.shortcuts import render

from .models import Menu


def display_all_menus(request):
    menus = Menu.objects.all()
    return render(request, 'tree_menu/index.html',
                  {'menus': menus})


def display_menu_item(request, menu_url: str = None, selected_url: str = None,
                      selected_level=None):
    return render(request, 'tree_menu/index.html',
                  {'menu_url': menu_url, 'selected_url': selected_url,
                   'selected_level': selected_level})

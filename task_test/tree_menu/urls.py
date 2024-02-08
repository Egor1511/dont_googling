from django.urls import path

from .views import display_menu_item, display_all_menus

urlpatterns = [
    path('', display_all_menus, name='all_menus'),
    path('<str:menu_url>/', display_menu_item, name='display_menu'),
    path('<str:menu_url>/<str:selected_url>/<int:selected_level>/', display_menu_item,
         name='display_menu_item'),
]

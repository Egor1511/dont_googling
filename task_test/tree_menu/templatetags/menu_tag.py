from typing import Any, Union

from django import template
from django.db.models import Q
from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(menu_url: str = None, selected_url: str = None,
              selected_level: Union[int, None] = None) -> dict[str, Any]:
    """
    Inclusion tag to render a menu.

    Args:
        menu_url (str, optional): The URL of the menu. Defaults to None.
        selected_url (str, optional): The URL of the selected menu item.
        Defaults to None.
        selected_level (int, optional): The selected level of menu items
        to display. Defaults to None.

    Returns:
        Dict[str, Any]: Dictionary containing menu data to be rendered in the
        template.
    """

    def get_context(menu_url: str) -> 'QuerySet[MenuItem]':
        """
        Retrieve menu items based on the provided menu URL.

        Args:
            menu_url (str): The URL of the menu.

        Returns:
            QuerySet[MenuItem]: QuerySet containing menu items.
        """
        if menu_url:
            context = MenuItem.objects.filter(
                Q(menu__url=menu_url) | Q(parent__menu__url=menu_url)
            ).select_related(
                'parent', 'menu'
            )
        else:
            context = MenuItem.objects.select_related('parent')
        return context

    def build_children(context: 'QuerySet[MenuItem]', parent_item: MenuItem,
                       selected_level: Union[int, None]) -> list[
        dict[str, Any]]:
        """
        Recursively build a dictionary representing children of a menu item.

        Args:
            context (QuerySet[MenuItem]): QuerySet containing menu items.
            parent_item (MenuItem): The parent menu item.
            selected_level (Union[int, None]): The selected level of menu items
            to display.

        Returns:
            List[Dict[str, Any]]: List of dictionaries representing children
            of the menu item.
        """
        children = [
            {item: {'parent': parent_item,
                    'children': build_children(context, item, selected_level)}
             }
            for item in context
            if item.parent == parent_item
               and (selected_level is None or item.level <= selected_level + 1)
        ]
        return children

    def build_menu_dict(context: 'QuerySet[MenuItem]',
                        selected_level: Union[int, None]) -> dict[str, Any]:
        """
        Build a dictionary representing the menu structure.

        Args:
            context (QuerySet[MenuItem]): QuerySet containing menu items.
            selected_level (Union[int, None]): The selected level of menu items
            to display.

        Returns:
            Dict[str, Any]: Dictionary containing the menu structure.
        """
        menu_dict = {
            item: {'parent': None,
                   'children': build_children(context, item, selected_level)}
            for item in context
            if item.parent is None
        }
        menu_dict = [menu_dict]
        return {'menu_dict': menu_dict, 'menu_url': menu_url,
                'selected_url': selected_url}

    context = get_context(menu_url)
    return build_menu_dict(context, selected_level)

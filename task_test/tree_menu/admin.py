from django.contrib import admin
from .models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin interface for managing menu items."""

    list_display = ('__str__', 'title', 'url', 'parent', 'menu',)
    prepopulated_fields = {'url': ('title',)}
    list_display_links = ('title', )
    readonly_fields = ('level', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Customize the form field for the ForeignKey 'parent'
        to exclude the current object.
        """
        if db_field.name == 'parent':
            kwargs['queryset'] = MenuItem.objects.exclude(
                pk=request.resolver_match.kwargs.get('object_id'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Admin interface for managing menus."""
    list_display = ('name', 'url', )
    prepopulated_fields = {'url': ('name', )}

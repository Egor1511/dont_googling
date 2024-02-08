from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """
    A model representing a menu.

    Attributes:
        name (CharField): The name of the menu.
        url (CharField): The URL of the menu.
    """

    name = models.CharField(
        verbose_name='Название меню',
        max_length=100,
    )
    url = models.CharField(
        verbose_name='URL',
        max_length=100,
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('name',)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    A model representing a menu item.

    Attributes:
        title (CharField): The title of the menu item.
        url (CharField): The URL of the menu item.
        parent (ForeignKey): The parent menu item.
        menu (ForeignKey): The menu to which the item belongs.
        level (PositiveSmallIntegerField): The level of nesting
        of the menu item.
    """

    OTS = '_'

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=100,
    )
    url = models.CharField(
        verbose_name='URL',
        max_length=100,
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Является подпунктом',
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Принадлежит меню',
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень вложенности',
        default=0,

    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('menu', 'parent__title')

    def __str__(self):
        return f'{self.OTS * self.level}{self.title}'

from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MenuItem


@receiver(post_save, sender=MenuItem)
def update_menu_item_level(sender, instance, created, **kwargs):
    """
    Signal receiver function to update the level of a MenuItem
    after it's saved. Based on its parent's level.
    """

    parent_level = instance.parent.level if instance.parent else -1
    instance.level = parent_level + 1

    MenuItem.objects.filter(pk=instance.pk).update(level=instance.level)



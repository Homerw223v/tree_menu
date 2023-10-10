from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Menu


@receiver(pre_save, sender=Menu)
def create_profile(sender, instance: Menu, **kwargs):
    """Create url when saving Menu instance"""
    instance.create_url()

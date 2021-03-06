# Signals sent by django after model instance is saved and deleted
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# Execute function when post signals are sent
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    # Update order total on line item update/ create
    instance.order.update_total()


# Execute function when save signals are sent
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    # Update order total on line item delete
    instance.order.update_total()

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like
from notifications.models import Notification


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    """
    Signal to create a notification when a like is created.
    This signal is triggered after a Like instance is saved.
    It checks if the like was newly created and if the owner of the like
    is different from the owner of the post. If so, it creates a notification
    for the post owner.
    """
    if created and instance.post.owner != instance.owner:
        Notification.objects.create(
            to_user=instance.post.owner,
            from_user=instance.owner,
            notification_type='like',
            post=instance.post
        )

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Follow
from notifications.models import Notification


@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    """
    Signal to create a notification when a follow is created.
    This signal is triggered after a Follower instance is saved.
    It checks if the follow was newly created and if the follower is different
    from the owner of the follow. If so, it creates a notification
    for the followed user.
    """
    if created and instance.followed != instance.owner:
        Notification.objects.create(
            to_user=instance.followed,
            from_user=instance.owner,
            notification_type='follow'
        )

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from notifications.models import Notification


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    """
    Signal to create a notification when a comment is created.
    This signal is triggered after a Comment instance is saved.
    It checks if the comment was newly created and if the owner of the comment
    is different from the owner of the post. If so, it creates a notification
    for the post owner.
    """
    if created and instance.post.owner != instance.owner:
        Notification.objects.create(
            to_user=instance.post.owner,
            from_user=instance.owner,
            notification_type='comment',
            post=instance.post,
            comment=instance
        )

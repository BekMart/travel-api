from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    ]

    to_user = models.ForeignKey(
        User, related_name='notifications', on_delete=models.CASCADE
    )
    from_user = models.ForeignKey(
        User, related_name='sent_notifications', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True
    )
    notification_type = models.CharField(
        max_length=10, choices=NOTIFICATION_TYPES
    )
    created_on = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.from_user} -> {self.to_user} ({self.notification_type})"

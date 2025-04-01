from django.db import models
from django.contrib.auth.models import User
from locations.models import Location


# Post model that represents a travel post
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_image_pr9kie'
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

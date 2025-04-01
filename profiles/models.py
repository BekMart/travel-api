from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Profile model that extends the User model
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ngcscr'
    )
    nationality = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    resides = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


# This function creates a profile for each user when the user is created.
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


# This saves the profile when the user is saved.
post_save.connect(create_profile, sender=User)

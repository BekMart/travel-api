from django.db import models
from django.utils.text import slugify
from django.db.models.functions import Lower


class Location(models.Model):
    """
    Model representing a travel location that can be associated with Posts.
    Includes automatic slug generation and name case-insensitive/uniqueness.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='locations/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='unique_location_name_ci'
            )
        ]

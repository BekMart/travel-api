from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model
    """
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'slug', 'image', 'description', 'posts_count']
        read_only_fields = ['name', 'slug']

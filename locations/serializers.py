from rest_framework import serializers
from .models import Location


# Serializer for the Location model
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'slug']

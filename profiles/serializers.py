from rest_framework import serializers
from .models import Profile


# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'content', 'image', 'nationality', 'age', 
            'resides', 'created_on', 'updated_on'
        ]

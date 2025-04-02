from rest_framework import serializers
from .models import Profile


# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the profile.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'content', 'image', 'nationality', 'age',
            'resides', 'created_on', 'updated_on', 'is_owner',
        ]

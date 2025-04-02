from rest_framework import serializers
from .models import Profile
from followers.models import Follow


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the profile.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_following_id(self, obj):
        """
        Get the ID of the follow instance if the user is authenticated and
        following the profile owner.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follow.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'content', 'image', 'nationality', 'age',
            'resides', 'created_on', 'updated_on', 'is_owner', 'following_id',
        ]

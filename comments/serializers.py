from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Return True if the requesting user is the owner of the comment
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        """
        Return human-readable creation time
        """
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        """
        Return human-readable updated time
        """
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'post', 'content', 'created_on', 'updated_on',
            'is_owner', 'profile_id', 'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    """
    post = serializers.ReadOnlyField(source='post.id')

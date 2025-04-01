from rest_framework import serializers
from .models import Post


# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'content', 'image', 'location',
            'created_on', 'updated_on'
        ]

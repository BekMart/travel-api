from rest_framework import serializers
from .models import Post
from locations.models import Location


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    location = serializers.CharField()

    def validate_image(self, value):
        """
        Validate the image size and dimensions.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Check if the current user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'content', 'image', 'location',
            'created_on', 'updated_on', 'is_owner', 'profile_id',
            'profile_image',
        ]

    def create(self, validated_data):
        """
        This method handles the creation of the location instance
        if it does not exist.
        """
        location_name = validated_data.pop('location')
        location, created = Location.objects.get_or_create(name=location_name)
        validated_data['location'] = location
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing post instance.
        This method handles the update of the location instance
        if the location name is provided.
        """
        location_name = validated_data.pop('location', None)
        if location_name:
            location, created = Location.objects.get_or_create(
                name=location_name
            )
            validated_data['location'] = location
        return super().update(instance, validated_data)

from rest_framework import serializers
from django.db.models import Count
from .models import Post
from locations.models import Location
from likes.models import Like
from locations.serializers import LocationSerializer


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    location = serializers.CharField(write_only=True)
    location_details = LocationSerializer(source='location', read_only=True)
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_location_details(self, obj):
        """
        Get the location details for the post.
        """
        return LocationSerializer(obj.location).data

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

    def get_like_id(self, obj):
        """
        Get the ID of the like if the user has liked the post.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'content', 'image', 'location',
            'location_details', 'created_on', 'updated_on', 'is_owner',
            'profile_id', 'profile_image', 'like_id', 'likes_count',
            'comments_count',
        ]

    def create(self, validated_data):
        """
        This method handles the creation of the location instance
        if it does not exist.
        """
        location_name = validated_data.pop('location').strip().lower()
        location, created = Location.objects.get_or_create(name=location_name)
        validated_data['location'] = location
        post = super().create(validated_data)

        try:
            popular_post_with_image = location.posts \
                .filter(image__isnull=False) \
                .annotate(likes_count=Count('likes')) \
                .order_by('-likes_count', '-created_on') \
                .first()
            if popular_post_with_image:
                location.image = popular_post_with_image.image
                location.save()
        except Exception as e:
            print("Error assigning location image:", e)

        post.refresh_from_db()
        return post

    def update(self, instance, validated_data):
        """
        Update an existing post instance.
        This method handles the update of the location instance
        if the location name is provided.
        """
        location_name = validated_data.pop('location', None)
        if location_name:
            location_name = location_name.strip().lower()
            location, created = Location.objects.get_or_create(
                name=location_name
            )
            validated_data['location'] = location
        return super().update(instance, validated_data)

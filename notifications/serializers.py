from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying notification details, including info about
    the users involved and optionally related posts or comments
    """
    from_user = serializers.StringRelatedField(read_only=True)
    from_user_profile_id = serializers.IntegerField(
        source='from_user.profile.id', read_only=True
    )
    to_user = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    comment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'from_user',
            'from_user_profile_id',
            'to_user',
            'notification_type',
            'post',
            'comment',
            'created_on',
            'is_read',
        ]


class ReadAllNotificationsSerializer(serializers.ModelSerializer):
    """
    Serializer for updating notifications, specifically to mark them as read
    Used when bulk-marking notifications
    """
    class Meta:
        model = Notification
        fields = ['is_read']

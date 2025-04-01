from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(generics.ListAPIView):
    """
    List all notifications
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

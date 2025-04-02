from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(generics.ListAPIView):
    """
    List all notifications
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of all the notifications for currently
        authenticated user.
        """
        return Notification.objects.filter(to_user=self.request.user).order_by(
            '-created_on')

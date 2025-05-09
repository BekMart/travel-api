from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer, ReadAllNotificationsSerializer


class NotificationList(generics.ListAPIView):
    """
    List all of a users notifications
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        List all notifications for currently authenticated user newest first
        """
        return Notification.objects.filter(to_user=self.request.user).order_by(
            '-created_on')


class UnreadNotificationList(generics.ListAPIView):
    """
    List only unread notifications for the current user
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            to_user=self.request.user,
            is_read=False
        ).order_by('-created_on')


class MarkNotificationRead(APIView):
    """
    Mark a single notification as read
    """
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        notification = get_object_or_404(
            Notification, pk=pk, to_user=request.user
        )
        notification.is_read = True
        notification.save()
        return Response({'status': 'notification marked as read'})


class MarkAllNotificationsRead(APIView):
    """
    Mark all notifications as read for currently authenticated user
    """
    serializer_class = ReadAllNotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        Notification.objects.filter(
            to_user=request.user, is_read=False).update(is_read=True)
        return Response({'status': 'all notifications marked as read'})

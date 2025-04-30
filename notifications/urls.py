from django.urls import path
from notifications import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view()),
    path('notifications/unread/', views.UnreadNotificationList.as_view()),
    path(
        'notifications/<int:pk>/mark-read/',
        views.MarkNotificationRead.as_view()
        ),
    path(
        'notifications/mark-all-read/',
        views.MarkAllNotificationsRead.as_view()
        )
]

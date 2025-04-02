from django.urls import path
from notifications import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view()),
    path('notifications/mark-read/', views.MarkAllNotificationsRead.as_view()),
]

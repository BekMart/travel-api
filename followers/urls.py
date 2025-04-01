from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowList.as_view()),
]

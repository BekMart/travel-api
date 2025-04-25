from django.urls import path
from .views import PostList, PostDetail, PostFeedList, TopPostList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/feed/', PostFeedList.as_view()),
    path('posts/popular/', TopPostList.as_view()),
]

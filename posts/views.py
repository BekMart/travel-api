from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    """
    List all posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

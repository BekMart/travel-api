from rest_framework import generics
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListAPIView):
    """
    List all likes
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

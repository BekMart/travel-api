from rest_framework import generics
from .models import Follow
from .serializers import FollowSerializer


class FollowList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    """
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

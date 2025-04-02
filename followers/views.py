from rest_framework import generics, permissions
from travel_api.permissions import IsOwnerOrReadOnly
from .models import Follow
from .serializers import FollowSerializer


class FollowList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the follow with the logged in user as the owner.
        """
        serializer.save(owner=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follow, or unfllow by id if owner.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsOwnerOrReadOnly]

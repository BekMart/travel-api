from django.db.models import Count
from rest_framework import generics, filters
from travel_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles with added fields
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    search_fields = [
        'owner__username',
        'content',
    ]
    filter_backends = [
            filters.OrderingFilter
        ]
    ordering_fields = [
        'post_count',
        'followers_count',
        'following_count',
        'owner__following__created_on',
        'owner__followed_created__on',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PopularProfilesList(generics.ListAPIView):
    """
    List profiles ordered by number of followers
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.annotate(
            followers_count=Count('owner__followed', distinct=True)
        ).order_by('-followers_count', 'owner__username')

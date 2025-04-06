from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from travel_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all posts or create if logged in.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',  # show all posts by a user
        'location__slug',  # show all posts in a location
        'likes__owner__profile',  # show all posts liked by a user
    ]
    ordering_fields = [
        'likes_count',  # show all posts ordered by likes
        'comments_count',  # show all posts ordered by comments
        'created_on',  # show all posts ordered by created date
        'updated_on',  # show all posts ordered by updated date
    ]

    def perform_create(self, serializer):
        """
        Save the post with the current user as the owner.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_on')


class PostFeedList(generics.ListAPIView):
    """
    List posts only from users the current user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',  # show all posts by a user
        'location__slug',  # show all posts in a location
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'created_on',
        'updated_on',
    ]

    def get_queryset(self):
        from followers.models import Follow

        user = self.request.user
        followed_users = Follow.objects.filter(owner=user).values_list('followed', flat=True)

        queryset = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True),
        ).filter(owner__in=followed_users).order_by('-created_on')

        return queryset

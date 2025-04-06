from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from travel_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from followers.models import Follow


class BasePostListView(generics.ListAPIView):
    """
    Base view for listing posts with common behaviour.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'location__name',
        'content',
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

    def get_base_queryset(self):
        """
        Shared queryset logic for post views.
        """
        return Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True),
        ).order_by('-created_on')


class PostList(BasePostListView, generics.ListCreateAPIView):
    """
    List all posts or create a new post if logged in.
    """
    def get_queryset(self):
        return self.get_base_queryset()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostFeedList(BasePostListView):
    """
    List posts only from users the current user follows.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = Follow.objects.filter(owner=user).values_list(
            'followed', flat=True)
        return self.get_base_queryset().filter(
            owner__in=followed_users).order_by('-created_on')


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

from rest_framework import generics
from django.db.models import Count
from .models import Location
from .serializers import LocationSerializer
from posts.models import Post
from posts.serializers import PostSerializer


class LocationList(generics.ListAPIView):
    """
    List all locations ordered by number of posts (popularity)
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.annotate(
        posts_count=Count('posts', distinct=True)
    ).order_by('-posts_count')


class LocationDetail(generics.RetrieveAPIView):
    """
    Retrieve a location by slug
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.annotate(
        posts_count=Count('posts', distinct=True)
    ).order_by('-posts_count')
    lookup_field = 'slug'


class LocationPostList(generics.ListAPIView):
    """
    List all posts for a specific location.
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(location__slug=slug).annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True),
        ).order_by('-id')

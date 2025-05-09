from rest_framework import generics, permissions
from travel_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given post,
        by filtering against a `post` query parameter in the URL.
        """
        post_id = self.request.query_params.get('post')
        if post_id:
            return Comment.objects.filter(post__id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        """
        Save the comment with the logged in user as the owner.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()

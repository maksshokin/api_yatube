from django.shortcuts import get_object_or_404

from posts.models import Group, Post, Comment
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets

from api.permissions import IsAuthor



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthor, permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthor, permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

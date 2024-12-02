from rest_framework import viewsets

from yatube_api.posts.models import Post
from yatube_api.yatube_api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
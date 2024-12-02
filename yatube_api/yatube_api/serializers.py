from rest_framework import serializers

from yatube_api.posts.models import Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Основной сериализатор."""
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'image',
            'pub_date',
            'group',
        )
        model = Post

from rest_framework import serializers

from blog.models import Comment


class CommentListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id', 'text' , 'parent_comment',
            'created_at', 'updated_at',
            'post_id', 'author_id'
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at',
            'post_id', 'author_id'
        )

from rest_framework import serializers

from blog.models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

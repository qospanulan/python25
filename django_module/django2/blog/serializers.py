from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['name', 'description']

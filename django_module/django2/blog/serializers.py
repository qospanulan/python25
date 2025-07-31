from rest_framework import serializers

from blog.models import Blog


class BlogListOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name']


# class BlogCreateInputSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Blog
#         fields = ['name', 'description', 'tags']


# class BlogCreateOutputSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Blog
#         fields = '__all__'


class BlogDetailOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class BlogFullUpdateInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['name', 'description']


class BlogStatusUpdateInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['status']


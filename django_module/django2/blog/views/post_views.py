from rest_framework import views, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from blog.services.post_service import get_post_service
from utils.serializers import inline_serializer


# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField()


class PostListAPIView(views.APIView):

    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        content = serializers.CharField(max_length=120)

        author = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "username": serializers.CharField()
            }
        )

        blog = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "name": serializers.CharField()
            }
        )

    def get(self, request):

        post_service = get_post_service()

        posts = post_service.get_all_posts()

        serializer = self.OutputSerializer(
            instance=posts,
            many=True
        )

        return Response(serializer.data)


class BlogPostListAPIView(views.APIView):

    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        content = serializers.CharField(max_length=120)
        # author =
        # blog =

    def get(self, request, blog_id: int):
        post_service = get_post_service()

        posts = post_service.get_all_posts_by_blog_id(
            blog_id=blog_id
        )

        serializer = self.OutputSerializer(
            instance=posts,
            many=True
        )

        return Response(serializer.data)


class PostCreateAPIView(views.APIView):

    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        content = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        content = serializers.CharField(max_length=120)
        # author =
        # blog =

    def post(self, request, blog_id: int):

        input_serializer = self.InputSerializer(
            data=request.data
        )

        input_serializer.is_valid(raise_exception=True)

        post_service = get_post_service()
        post = post_service.create_post(
            author_id=request.user.id,
            blog_id=blog_id,
            content=input_serializer.validated_data.get("content")
        )

        output_serializer = self.OutputSerializer(instance=post)

        return Response(output_serializer.data)

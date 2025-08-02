from django.db import IntegrityError
from rest_framework import views, serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from blog.service_factory import get_service
from blog.services.post_service import PostService, get_post_service


class PostListAPIView(views.APIView):

    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        content = serializers.CharField(max_length=120)
        # author =
        # blog =

    def get(self, request):

        # post_service = PostService()
        # post_service = get_service("post_service")
        post_service = get_post_service()

        print("== GET POSTS ================================")
        print(f"{post_service}")
        print("==================================")

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
        """

        cache = {
            "get_post_service": <blog.services.post_service.PostService object at 0x7e15124a7010>
        }

        """
        # post_service = PostService()
        # post_service = get_service("post_service")
        post_service = get_post_service()

        print("== GET POSTS by BLOG ================================")
        print(f"{post_service}")
        print("==================================")

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

        post_service = PostService()
        post = post_service.create_post(
            author_id=request.user.id,
            blog_id=blog_id,
            content=input_serializer.validated_data.get("content")
        )

        output_serializer = self.OutputSerializer(instance=post)

        return Response(output_serializer.data)

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import views, status, serializers

from blog.serializers import (
    BlogListOutputSerializer, BlogDetailOutputSerializer,
    BlogFullUpdateInputSerializer, BlogStatusUpdateInputSerializer
)
from blog.services.blog_service import BlogService


class BlogListAPIView(views.APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        service = BlogService()
        blogs = service.get_all_blogs()

        serializer = BlogListOutputSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogCreateAPIView(views.APIView):

    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=120)
        description = serializers.CharField()
        tags = serializers.ListSerializer(
            child=serializers.IntegerField(),
            allow_null=True,
            allow_empty=True,
            default=[]
        )

    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=120)
        description = serializers.CharField()

        author = serializers.IntegerField()
        status = serializers.CharField(max_length=100)
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()

        tags = serializers.ListSerializer(
            child=serializers.IntegerField(),
            allow_null=True,
            allow_empty=True,
            default=[]
        )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        service = BlogService()
        blog = service.create_blog(
            user_id=request.user.id,
            data=serializer.validated_data
        )

        return Response(
            self.OutputSerializer(instance=blog).data
        )


class BlogDetailAPIView(views.APIView):

    permission_classes = [AllowAny]

    def get(self, request, blog_id):
        try:

            service = BlogService()

            blog = service.get_blog_by_id(
                blog_id=blog_id
            )

            serializer = BlogDetailOutputSerializer(
                instance=blog
            )

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"detail": "No Blog matches the given query."},
                status=status.HTTP_404_NOT_FOUND
            )


class BlogUpdateAPIView(views.APIView):

    def put(self, request, blog_id):

        try:
            serializer = BlogFullUpdateInputSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            service = BlogService()
            blog = service.update_blog(
                blog_id=blog_id,
                data=serializer.validated_data
            )

            return Response(
                BlogDetailOutputSerializer(
                    instance=blog
                ).data
            )
        except Exception as e:
            return Response(
                {"message": f"Error: {e}"},
                status=status.HTTP_400_BAD_REQUEST
            )


class BlogUpdateStatusAPIView(views.APIView):

    def patch(self, request, blog_id):
        try:
            serializer = BlogStatusUpdateInputSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            service = BlogService()
            blog = service.update_status(
                blog_id=blog_id,
                new_status=serializer.validated_data.get('status')
            )

            return Response(
                BlogDetailOutputSerializer(
                    instance=blog
                ).data
            )
        except Exception as e:
            return Response(
                {"message": f"Error: {e}"},
                status=status.HTTP_400_BAD_REQUEST
            )


class BlogDeleteAPIView(views.APIView):

    def delete(self, request, blog_id):

        service = BlogService()
        service.delete_blog(blog_id=blog_id)

        return Response(
            {"message": "Successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

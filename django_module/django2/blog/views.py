from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views, status

from blog.serializers import (
    BlogListOutputSerializer, BlogCreateInputSerializer,
    BlogCreateOutputSerializer, BlogDetailOutputSerializer,
    BlogFullUpdateInputSerializer, BlogStatusUpdateInputSerializer
)
from blog.services.blog_service import BlogService


class BlogListAPIView(views.APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        service = BlogService()
        blogs = service.get_all_blogs()

        serializer = BlogListOutputSerializer(blogs, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BlogCreateInputSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        service = BlogService()
        blog = service.create_blog(
            user_id=request.user_id,
            data=serializer.validated_data
        )

        return Response(
            BlogCreateOutputSerializer(instance=blog).data
        )


class BlogDetailDeleteAPIView(views.APIView):

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



    def delete(self, request, blog_id):

        service = BlogService()
        service.delete_blog(blog_id=blog_id)

        return Response(
            {"message": "Successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

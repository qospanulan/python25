import json

from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import views, status, serializers

from blog.services.blog_service import get_blog_service
from utils.parsers import parse_list_from_str
from utils.serializers import inline_serializer


class BlogListAPIView(views.APIView):

    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        count = serializers.IntegerField()
        next = serializers.CharField()
        previous = serializers.CharField()
        results = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "name": serializers.CharField(max_length=120),

                "author": inline_serializer(
                    fields={
                        "id": serializers.IntegerField(),
                        "username": serializers.CharField()
                    }
                )
            },
            many=True
        )

    def get(self, request):

        # author_ids: list[str] | None = request.query_params.getlist("author_ids")
        author_ids: str | None = request.query_params.get("author_ids")
        name: str | None = request.query_params.get("name")

        page: int = request.query_params.get("page", 1)

        if author_ids:
            # author_ids: list = parse_list_from_str(author_ids)
            author_ids: list = json.loads(author_ids)

        service = get_blog_service()
        blogs = service.get_all_blogs(
            author_ids=author_ids,
            name=name,
            page=page,
            url=request.build_absolute_uri()
        )

        serializer = self.OutputSerializer(blogs)

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
        id = serializers.IntegerField()
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

        service = get_blog_service()
        blog = service.create_blog(
            user_id=request.user.id,
            data=serializer.validated_data
        )

        output_serializer = self.OutputSerializer(instance=blog)

        return Response(output_serializer.data)


class BlogDetailAPIView(views.APIView):

    permission_classes = [AllowAny]

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=120)
        description = serializers.CharField()

        author = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "username": serializers.CharField()
            }
        )

        post_set = inline_serializer(
            fields={
                "id": serializers.IntegerField(),
                "content": serializers.CharField()
            },
            many=True
        )

        status = serializers.CharField(max_length=100)
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()

        tags = serializers.ListSerializer(
            child=serializers.IntegerField(),
            allow_null=True,
            allow_empty=True,
            default=[]
        )

    def get(self, request, blog_id):
        try:

            service = get_blog_service()

            blog = service.get_blog_by_id(
                blog_id=blog_id
            )

            serializer = self.OutputSerializer(
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

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=120)
        description = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
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

    def put(self, request, blog_id):

        try:
            serializer = self.InputSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            service = get_blog_service()
            blog = service.update_blog(
                blog_id=blog_id,
                data=serializer.validated_data
            )

            return Response(
                self.OutputSerializer(
                    instance=blog
                ).data
            )
        except Exception as e:
            return Response(
                {"message": f"Error: {e}"},
                status=status.HTTP_400_BAD_REQUEST
            )


class BlogUpdateStatusAPIView(views.APIView):

    class InputSerializer(serializers.Serializer):
        status = serializers.CharField(max_length=100)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
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

    def patch(self, request, blog_id):
        try:
            serializer = self.InputSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            service = get_blog_service()
            blog = service.update_status(
                blog_id=blog_id,
                new_status=serializer.validated_data.get('status')
            )

            return Response(
                self.OutputSerializer(
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

        service = get_blog_service()
        service.delete_blog(blog_id=blog_id)

        return Response(
            {"message": "Successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

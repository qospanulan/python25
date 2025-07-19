from django.db.models import QuerySet, Q
from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views, status

from blog.constants import HIDDEN
from blog.models import Blog
from blog.serializers import (
    BlogListOutputSerializer, BlogCreateInputSerializer,
    BlogCreateOutputSerializer, BlogDetailOutputSerializer, BlogFullUpdateInputSerializer,
    BlogStatusUpdateInputSerializer
)


class BlogListAPIView(views.APIView):

    def get(self, request):
        blogs: QuerySet[Blog] = Blog.objects.all()
        # blogs: QuerySet[Blog] = Blog.objects.filter(
        #     ~Q(status=HIDDEN)
        # )

        return Response(
            BlogListOutputSerializer(
                blogs,
                many=True
            ).data
        )

    def post(self, request):
        data = request.data

        serializer = BlogCreateInputSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        blog: Blog = serializer.save()

        return Response(
            BlogCreateOutputSerializer(instance=blog).data
        )


class BlogDetailDeleteAPIView(views.APIView):

    def get(self, request, blog_id):
        blog: Blog = Blog.objects.get(id=blog_id)

        serializer = BlogDetailOutputSerializer(
            instance=blog
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, blog_id):

        try:
            serializer = BlogFullUpdateInputSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            blog: Blog = Blog.objects.get(id=blog_id)

            for key, value in serializer.validated_data.items():
                setattr(blog, key, value)

            # blog.name = serializer.validated_data.get("name")
            # blog.description = serializer.validated_data.get("description")

            blog.save()

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

            blog: Blog = Blog.objects.get(id=blog_id)

            blog.status = serializer.validated_data.get("status")

            blog.save()

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
        blog: Blog = Blog.objects.get(id=blog_id)

        blog.delete()

        return Response(
            {"message": "Successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )



@api_view(http_method_names=['GET'])
def get_blog_list(request):
    blogs: QuerySet[Blog] = Blog.objects.all()

    # blogs_json = []

    # for blog in blogs:
    # blog_json = {
    #     "name": blog.name,
    #     "description": blog.description,
    #     "created_at": blog.created_at,
    #     "updated_at": blog.updated_at
    # }

    # blog_json = {}

    # for field in blog._meta.get_fields():
    #     if not field.is_relation:
    #         blog_json[field.name] = getattr(blog, field.name)

    # blog_json = model_to_dict(blog)

    # blog_json = BlogListSerializer(blog).data
    # blogs_json.append(blog_json)

    # blogs_json = BlogListSerializer(blogs, many=True).data
    return Response(
        BlogListOutputSerializer(
            blogs,
            many=True
        ).data
    )


@api_view(http_method_names=['GET', 'POST'])
def test_health(request: HttpRequest):
    if request.method == "GET":
        return Response({"msg": "Hello World!"})

    elif request.method == "POST":
        print(request.data)
        return Response({"msg": "Post method handled!"})

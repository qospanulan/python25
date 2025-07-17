from django.db.models import QuerySet
from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views

from blog.models import Blog
from blog.serializers import BlogSerializer, BlogCreateSerializer


class BlogListAPIView(views.APIView):

    def get(self, request):
        blogs: QuerySet[Blog] = Blog.objects.all()

        return Response(
            BlogSerializer(
                blogs,
                many=True
            ).data
        )

    def post(self, request):

        data = request.data

        serializer = BlogCreateSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        blog: Blog = serializer.save()

        return Response(
            BlogSerializer(instance=blog).data
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
        BlogSerializer(
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

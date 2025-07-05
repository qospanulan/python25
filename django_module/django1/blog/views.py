from django.db.models import F
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render

from blog.models import Post

# Function Based View
# Class Based View

# Params - GET
# Payload/Body - POST


def get_posts_list(request):

    posts = Post.objects.all()

    template_name = "blog/posts_list.html"
    context = {
        "posts": posts
    }

    return render(
        request=request,
        template_name=template_name,
        context=context
    )


def get_post_detail(request, post_id):

    print("======================================")
    print(f"Post id: {post_id}")
    print("======================================")

    return HttpResponse("test")


def get_hello_world(request: HttpRequest):

    params: dict = request.GET
    name = params.get("name", "World")
    context = {
        "name_value": name
    }

    # template: Template = loader.get_template("blog/hello_world.html")
    # return HttpResponse(template.render(context, request))

    return render(
        request=request,
        template_name="blog/hello_world.html",
        context=context
    )

def get_json_posts(request):

    posts = Post.objects.all()
    # posts = Post.objects.filter(created_at=F("updated_at"))

    return JsonResponse([
        {
            "id": post.id,
            "content": post.content,
            "blog_id": post.blog_id
        } for post in posts
    ], safe=False)
    #
    # return JsonResponse([
    #     {
    #         "id": 1,
    #         "content": "Hello",
    #         "blog_id": 1
    #     },
    #     {
    #         "id": 2,
    #         "content": "World",
    #         "blog_id": 1
    #     }
    # ], safe=False)

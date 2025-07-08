from django.db.models import F
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from blog.models import Post, Blog


# Function Based View
# Class Based View

# Params - GET
# Payload/Body - POST
# Create Read Update Delete

def create_post(request: HttpRequest):
    """
    GET -> Форму для заполнения при создании поста
    POST -> Обработка при нажатии кнопки создать
    """

    print(f"Method is: {request.method}")

    if request.method == 'GET':
        print("================================================")
        print("in GET method")
        print("================================================")
        template_name = "blog/post_create.html"

        return render(
            request=request,
            template_name=template_name
        )

    elif request.method == 'POST':
        print("================================================")
        print("in POST method:")
        print(request.POST)
        print("================================================")
        content = request.POST.get("content")
        blog_id = int(request.POST.get("blog_id"))

        blog = Blog.objects.get(id=blog_id)

        post = Post(
            content=content,
            blog=blog
        )

        post.save()

        return redirect('get_post_detail', post.id)

    else:
        return HttpResponse("Method Not Allowed", status=400)


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

    # post = Post.objects.filter(id=post_id)[0]
    post = Post.objects.get(id=post_id)

    template_name = "blog/post_detail.html"
    context = {
        "post": post
    }

    return render(
        request=request,
        template_name=template_name,
        context=context
    )


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

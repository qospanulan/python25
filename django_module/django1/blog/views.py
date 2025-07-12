from django import forms, views
from django.db.models import F
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from blog.models import Post, Blog


# Function Based View
# Class Based View

# Params - GET
# Payload/Body - POST
# Create Read Update Delete


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'blog')
        labels = {
            'content': 'Новый контент'
        }

# class PostCreateForm(forms.Form):
#     content = forms.TextInput()

class PostCreateView(views.View):

    def get(self, request):
        template_name = "blog/post_create.html"

        form = PostCreateForm()
        return render(
            request=request,
            template_name=template_name,
            context={
                "form": form
            }
        )

    def post(self, request):
        form = PostCreateForm(request.POST)

        if form.is_valid():
            # if not form.cleaned_data.get("content").endswith('...'):
            #     form.cleaned_data["content"] += "..."

            new_post = form.save()

            return redirect(
                'get_post_detail',
                new_post.id
            )

def create_post(request: HttpRequest):
    """
    GET -> Форму для заполнения при создании поста
    POST -> Обработка при нажатии кнопки создать
    """

    if request.method == 'GET':
        template_name = "blog/post_create.html"

        form = PostCreateForm()
        return render(
            request=request,
            template_name=template_name,
            context={
                "form": form
            }
        )

    elif request.method == 'POST':

        form = PostCreateForm(request.POST)

        if form.is_valid():

            # if not form.cleaned_data.get("content").endswith('...'):
            #     form.cleaned_data["content"] += "..."

            print("=======================================")
            print(f"form.cleaned_data: {form.cleaned_data}")
            print(f"form.data: {form.data}")
            print(f"request.POST: {request.POST}")
            print("=======================================")

            new_post = form.save()

            return redirect(
                'get_post_detail',
                new_post.id
            )

    else:
        return HttpResponse("Method Not Allowed", status=400)


def create_post_old(request: HttpRequest):
    """
    GET -> Форму для заполнения при создании поста
    POST -> Обработка при нажатии кнопки создать
    """

    print(f"Method is: {request.method}")

    if request.method == 'GET':
        print("================================================")
        print("in GET method")
        print("================================================")
        template_name = "blog/post_create_old.html"
        blogs = Blog.objects.all()

        return render(
            request=request,
            template_name=template_name,
            context={
                "blogs": blogs
            }
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


class PostListView(views.View):

    def get(self, request):
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

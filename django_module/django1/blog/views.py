from django.http import JsonResponse
from django.shortcuts import render

from blog.models import Post


def get_posts(request):

    posts = Post.objects.all()

    return JsonResponse([
        {
            "id": post.id,
            "content": post.content,
            "blog_id": post.blog_id
        } for post in posts
    ], safe=False)

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

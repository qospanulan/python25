from django.urls import path

from blog.views import get_hello_world, get_json_posts, get_posts_list, get_post_detail

urlpatterns = [
    path('posts/', get_posts_list, name="get_posts_list"),  # /blog/posts/
    path('posts/<int:post_id>/', get_post_detail, name="get_post_detail"),  # /blog/posts/1/
    path('hello_world/', get_hello_world, name="get_hello_world"),  # /blog/hello_world/
    path('posts/json/', get_json_posts, name="get_json_post"),  # /blog/posts/json/
    # path('comments/', get_posts, name="get_comments"),
]

from django.urls import path

from blog.views import get_posts

urlpatterns = [
    path('posts/', get_posts, name="get_post"),
    path('comments/', get_posts, name="get_comments"),
]

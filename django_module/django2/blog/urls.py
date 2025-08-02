from django.urls import path

from blog.views.blog_views import (
    BlogListAPIView, BlogDetailAPIView,
    BlogUpdateAPIView, BlogDeleteAPIView,
    BlogUpdateStatusAPIView, BlogCreateAPIView
)

from blog.views.post_views import (
    PostListAPIView, BlogPostListAPIView, PostCreateAPIView
)

urlpatterns = [
    # == BLOG ===============
    path('', BlogListAPIView.as_view(), name='get_blog_list'),  # /blog/
    path('create/', BlogCreateAPIView.as_view(), name='create_blog'),  # /blog/create/
    path('<int:blog_id>/', BlogDetailAPIView.as_view(), name='get_blog_detail'),  # /blog/2/
    path(
        '<int:blog_id>/update/',
        BlogUpdateAPIView.as_view(),
        name='update_blog'
    ),  # /blog/2/update/
    path(
        '<int:blog_id>/update/status/',
        BlogUpdateStatusAPIView.as_view(),
        name='update_blog_status'
    ),  # /blog/2/update/status/
    path(
        '<int:blog_id>/delete/',
        BlogDeleteAPIView.as_view(),
        name='delete_blog'
    ),  # /blog/2/delete/

    # == POST ===============

    path('posts/', PostListAPIView.as_view(), name="get_post_list"),  # /blog/posts/
    path('<int:blog_id>/posts/', BlogPostListAPIView.as_view(), name="get_post_list_by_id"),  # /blog/2/posts/

    path(
        '<int:blog_id>/posts/create/',
        PostCreateAPIView.as_view(),
        name="get_post_list_by_id"
    )  # /blog/2/posts/create

]


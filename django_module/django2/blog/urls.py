from django.urls import path

from blog.views import (
    BlogListAPIView, BlogDetailAPIView, BlogUpdateAPIView, BlogDeleteAPIView, BlogUpdateStatusAPIView
)

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='get_blog_list'),  # /blog/
    path('create/', BlogListAPIView.as_view(), name='create_blog'),  # /blog/create/
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
]


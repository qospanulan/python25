from django.urls import path

from blog.views import (
    test_health, get_blog_list,
    BlogListAPIView, BlogDetailDeleteAPIView
)

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='get_blog_list'),  # /blog/
    path('<int:blog_id>/', BlogDetailDeleteAPIView.as_view(), name='get_blog_detail'),  # /blog/2/
    path('health/', test_health, name='test_health'),  # /blog/health/
]

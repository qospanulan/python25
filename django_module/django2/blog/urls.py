from django.urls import path

from blog.views import test_health, get_blog_list, BlogListAPIView

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='get_blog_list'),  # /blog/
    path('health/', test_health, name='test_health'),  # /blog/health/
]
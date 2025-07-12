from django.urls import path

from blog.views import test_health, get_blog_list

urlpatterns = [
    path('', get_blog_list, name='get_blog_list'),  # /blog/
    path('health/', test_health, name='test_health'),  # /blog/health/
]
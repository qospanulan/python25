from django.urls import path

from authorization.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login")
]

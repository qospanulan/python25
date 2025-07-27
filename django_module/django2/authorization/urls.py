from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authorization.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),  # /auth/register/
    path('login/', LoginAPIView.as_view(), name="login"),  # /auth/login/
    # JWT TOKEN AUTH
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # /auth/token/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # /auth/token/refresh/
]

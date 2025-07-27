from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authorization.serializers import UserCreateSerializer, UserLoginSerializer


class LoginAPIView(views.APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data.get("username"),
            password=serializer.validated_data.get("password")
        )

        login(request, user)

        return Response(
            {"detail": "Logged in!"}
        )


class RegisterAPIView(views.APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.validated_data["password"] = make_password(
            password=serializer.validated_data["password"]
        )

        user: get_user_model() = serializer.save()

        return Response(
            UserCreateSerializer(instance=user).data
        )

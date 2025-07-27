from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


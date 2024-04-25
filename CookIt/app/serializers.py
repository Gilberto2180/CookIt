from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from . import models

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "password"]


class UserComplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsuarioComplementacion
        fields = "__all__"

from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from . import models

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]

class UserComplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsuarioComplementacion
        fields = "__all__"

class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alergia
        fields = "__all__"

class ImagenRecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImagenReceta
        fields = "__all__"

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorito
        fields = "__all__"

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingrediente
        fields = "__all__"

class ListaDeComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ListaDeCompras
        fields = "__all__"

class PlaneacionSemanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaneacionSemanal
        fields = "__all__"


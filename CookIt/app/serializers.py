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


class RecetaSerializer(serializers.ModelSerializer):
    imagenes = ImagenRecetaSerializer(many=True, read_only=True)
    imagenes_subidas = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, 
            allow_empty_file=False, 
            use_url=False
        ),
        write_only=True
    )

    ingredientes = serializers.PrimaryKeyRelatedField(
        queryset=models.Ingrediente.objects.all(),
        many=True
    )

    class Meta:
        model = models.Receta
        fields = "__all__"
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("imagenes_subidas")
        ingredientes_data = validated_data.pop("ingredientes", [])

        recipe = models.Receta.objects.create(**validated_data)

        for image in uploaded_images:
            new_recipe_images = models.ImagenReceta.objects.create(
                receta=recipe, 
                imagen=image
            )

        for ingrediente in ingredientes_data:
            recipe.ingredientes.add(ingrediente)
            
        return recipe

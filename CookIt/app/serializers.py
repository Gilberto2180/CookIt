from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from . import models

User = get_user_model()


class UserComplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsuarioComplementacion
        fields = "__all__"


class ComentarioSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        source='usuario', 
        write_only=True
    )
    usuario = UserCreateSerializer(read_only=True)  
    class Meta:
        model = models.Comentario
        fields = "__all__"


class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alergia
        fields = "__all__"


class ImagenRecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImagenReceta
        fields = ["id", "imagen"]


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


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = "__all__"


class RecetaSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    imagenes = ImagenRecetaSerializer(many=True, read_only=True)
    usuario = UserCreateSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        source='usuario', 
        write_only=True
    )
    imagenes_subidas = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, 
            allow_empty_file=False, 
            use_url=False
        ),
        write_only=True
    )

    ingredientes_post = serializers.PrimaryKeyRelatedField(
        queryset=models.Ingrediente.objects.all(),
        many=True,
        write_only=True
    )

    categorias_post = serializers.PrimaryKeyRelatedField(
        queryset=models.Categoria.objects.all(),
        many=True,
        write_only=True
    )

    ingredientes = IngredienteSerializer(many=True, read_only=True)
    categorias = CategoriaSerializer(many=True, read_only=True)

    class Meta:
        model = models.Receta
        fields = "__all__"
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("imagenes_subidas")
        ingredientes_data = validated_data.pop("ingredientes_post", [])
        categories_data = validated_data.pop("categorias_post", [])

        recipe = models.Receta.objects.create(**validated_data)

        for image in uploaded_images:
            new_recipe_images = models.ImagenReceta.objects.create(
                receta=recipe, 
                imagen=image
            )

        for ingrediente in ingredientes_data:
            recipe.ingredientes.add(ingrediente)
        
        for category in categories_data:
            recipe.categorias.add(category)
            
        return recipe


class ComidaSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ComidasPlaneacion
        fields = "__all__"


class ComidasSerializer(serializers.ModelSerializer):
    desayuno = RecetaSerializer(read_only=True)
    colacion = RecetaSerializer(read_only=True)
    comida = RecetaSerializer(read_only=True)
    colacion2 = RecetaSerializer(read_only=True)
    cena = RecetaSerializer(read_only=True)

    class Meta:
        model = models.ComidasPlaneacion
        fields = "__all__"


class PlaneacinSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaneacionSemanal
        fields = "__all__"


class PlaneacionSemanalSerializer(serializers.ModelSerializer):
    dia1 = ComidasSerializer(read_only=True)
    dia2 = ComidasSerializer(read_only=True)
    dia3 = ComidasSerializer(read_only=True)
    dia4 = ComidasSerializer(read_only=True)
    dia5 = ComidasSerializer(read_only=True)
    dia6 = ComidasSerializer(read_only=True)
    dia7 = ComidasSerializer(read_only=True)

    class Meta:
        model = models.PlaneacionSemanal
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    recetas = RecetaSerializer(many=True, read_only=True)
    planeacion = PlaneacionSemanalSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "recetas", "planeacion"]

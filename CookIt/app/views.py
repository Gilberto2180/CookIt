from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from . import models, serializers


class UserComplementationModelViewSet(ModelViewSet):
    serializer_class = serializers.UserComplementationSerializer
    queryset = models.UsuarioComplementacion.objects.all()


class AlergiaViewSet(viewsets.ModelViewSet):
    queryset = models.Alergia.objects.all()
    serializer_class = serializers.AlergiaSerializer


class ImagenRecetaViewSet(viewsets.ModelViewSet):
    queryset = models.ImagenReceta.objects.all()
    serializer_class = serializers.ImagenRecetaSerializer


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = models.Favorito.objects.all()
    serializer_class = serializers.FavoritoSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = models.Ingrediente.objects.all()
    serializer_class = serializers.IngredienteSerializer


class ListaDeComprasViewSet(viewsets.ModelViewSet):
    queryset = models.ListaDeCompras.objects.all()
    serializer_class = serializers.ListaDeComprasSerializer


class PlaneacionSemanalViewSet(viewsets.ModelViewSet):
    queryset = models.PlaneacionSemanal.objects.all()
    serializer_class = serializers.PlaneacionSemanalSerializer


class RecetaViewSet(ModelViewSet):
    serializer_class = serializers.RecetaSerializer
    queryset = models.Receta.objects.all()

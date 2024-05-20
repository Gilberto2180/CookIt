from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from django.shortcuts import render
from . import models, serializers


class UserComplementationModelViewSet(ModelViewSet):
    serializer_class = serializers.UserComplementationSerializer
    queryset = models.UsuarioComplementacion.objects.all()


class AlergiaViewSet(viewsets.ModelViewSet):
    queryset = models.Alergia.objects.all()
    serializer_class = serializers.AlergiaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComentarioSerializer
    queryset = models.Comentario.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriaSerializer
    queryset = models.Categoria.objects.all()


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


class ComidasViewSet(viewsets.ModelViewSet):
    queryset = models.ComidasPlaneacion.objects.all()
    serializer_class = serializers.ComidasSerializer


def AccountActivation(request, uid, token):
    return render(request, "activation/activation.html", {
        "uid": uid,
        "token": token
    })

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UsuarioComplementacion(models.Model):
    nombre_completo = models.CharField(max_length=100)
    preferencias_dieteticas = models.CharField(max_length=200)
    fecha_nacimiento = models.DateTimeField()
    alergias = models.CharField(max_length=300)
    tipo_cocina_favorita = models.CharField(max_length=60)
    info = models.OneToOneField(User, on_delete=models.CASCADE)

class Favorito(models.Model):
    ranking_favorito = models.IntegerField(default=20)
    fecha_marcada = models.DateTimeField()
    veces_vista = models.IntegerField(default=600)

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=300)
    calorias = models.BigIntegerField()
    origen_receta = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=50)
    pasos = models.TextField(max_length=3000)
    imagenes = models.ImageField(upload_to='recetas/', blank=True, null=True)

class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=300)

class ListaDeCompras(models.Model):
    fecha_creacion = models.DateTimeField()
    frutas = models.TextField(max_length=3000)
    verduras = models.TextField(max_length=3000)
    medida = models.TextField(max_length=4000)
    productos_origen_animal = models.TextField(max_length=3000)
    liquidos = models.TextField(max_length=3000)
    legumbres = models.TextField(max_length=3000)
    cereales = models.TextField(max_length=3000)

class PlaneacionSemanal(models.Model):
    dia_inicio = models.DateTimeField()
    dia_finalizacion = models.DateTimeField()
    comida_del_dia = models.TextField(max_length=3000)
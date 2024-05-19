from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username, email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.username


class Alergia(models.Model):
    nombre_alergia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_alergia


class ImagenReceta(models.Model):
    imagen = models.ImageField(upload_to='recetas/')
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name="imagenes")


class UsuarioComplementacion(models.Model):
    preferencias_dieteticas = models.CharField(max_length=200)
    fecha_nacimiento = models.DateTimeField()
    alergias = models.ManyToManyField(Alergia)
    tipo_cocina_favorita = models.CharField(max_length=60)
    info = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )


class Favorito(models.Model):
    ranking_favorito = models.IntegerField(default=20)
    fecha_marcada = models.DateTimeField()
    veces_vista = models.IntegerField(default=600)


class Ingrediente(models.Model):
    nombre_ingrediente = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre_ingrediente


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre_receta = models.CharField(max_length=300)
    calorias = models.BigIntegerField()
    origen_receta = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=50)
    pasos = models.TextField(max_length=3000)
    tiempo_preparacion = models.CharField(max_length=50, null=True, blank=True)
    categorias = models.ManyToManyField(Categoria)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nombre_receta


class Comentario(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario"
    )
    contenido = models.TextField()
    receta = models.ForeignKey(
        Receta, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="comentarios"
    )


class ListaDeCompras(models.Model):
    fecha_creacion = models.DateTimeField()
    frutas = models.TextField(max_length=3000)
    verduras = models.TextField(max_length=3000)
    medida = models.TextField(max_length=4000)
    productos_origen_animal = models.TextField(max_length=3000)
    liquidos = models.TextField(max_length=3000)
    legumbres = models.TextField(max_length=3000)
    cereales = models.TextField(max_length=3000)

    def __str__(self):
        return self.fecha_creacion


class PlaneacionSemanal(models.Model):
    dia_inicio = models.DateTimeField()
    dia_finalizacion = models.DateTimeField()
    comida_del_dia = models.TextField(max_length=3000)

    def __str__(self):
        return self.dia_inicio

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


class ImagenReceta(models.Model):
    imagen = models.ImageField(upload_to='recetas/')
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name="imagenes")


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
    tiempo_preparacion = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    categorias = models.ManyToManyField(Categoria)
    ingredientes = models.ManyToManyField(Ingrediente)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="recetas"
    )

    def __str__(self):
        return self.nombre_receta


class Favorito(models.Model):
    usuario = models.ManyToManyField(User)
    recetas = models.ManyToManyField(Receta)


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


class UsuarioComplementacion(models.Model):
    alergias = models.ManyToManyField(Alergia, blank=True)
    info = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="info"
    )
    recetas_favoritas = models.ManyToManyField(Receta, blank=True)
    lista_compras = models.ManyToManyField(Ingrediente, blank=True)
    foto_perfil = models.ImageField(null=True, blank=True)


def create_usuario_complementacion(sender, instance, created, **kwargs):
    if created:
        UsuarioComplementacion.objects.create(info=instance)


models.signals.post_save.connect(create_usuario_complementacion, sender=User)


class ComidasPlaneacion(models.Model):
    desayuno = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        related_name='comidasplaneacion_desayuno'
    )
    colacion = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        related_name='comidasplaneacion_colacion'
    )
    comida = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        related_name='comidasplaneacion_comida'
    )
    colacion2 = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        related_name='comidasplaneacion_colacion2'
    )
    cena = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        related_name='comidasplaneacion_cena'
    )


class PlaneacionSemanal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="planeacion")
    dia_inicio = models.DateTimeField(null=True, blank=True)
    dia_finalizacion = models.DateTimeField(null=True, blank=True)
    dia1 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia1")
    dia2 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia2")
    dia3 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia3")
    dia4 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia4")
    dia5 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia5")
    dia6 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia6")
    dia7 = models.OneToOneField(ComidasPlaneacion, on_delete=models.CASCADE, null=True, blank=True, related_name="dia7")

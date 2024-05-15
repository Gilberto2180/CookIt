from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Alergia)
admin.site.register(models.ImagenReceta)
admin.site.register(models.UsuarioComplementacion)
admin.site.register(models.Favorito)
admin.site.register(models.Receta)
admin.site.register(models.Ingrediente)
admin.site.register(models.ListaDeCompras)
admin.site.register(models.PlaneacionSemanal)
admin.site.register(models.Categoria)

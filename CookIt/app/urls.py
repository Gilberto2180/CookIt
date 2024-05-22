from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("userscomp", views.UserComplementationModelViewSet)
router.register(r'alergia', views.AlergiaViewSet)
router.register(r'imagenreceta', views.ImagenRecetaViewSet)
router.register(r'favorito', views.FavoritoViewSet)
router.register(r'ingrediente', views.IngredienteViewSet)
router.register(r'planeacionsemanal', views.PlaneacionSemanalViewSet)
router.register(r'recetas', views.RecetaViewSet)
router.register(r'comentarios', views.ComentarioViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'comidas', views.ComidasViewSet)
router.register(r'sendcomidas', views.ComidasSendViewSet, basename="dasd")
router.register(r'sendplaneacion', views.PlaneacionSendViewSet, basename="sendplaneacion")
router.register("avisos", views.AvisosViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    path("activate/<str:uid>/<str:token>/", views.AccountActivation)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

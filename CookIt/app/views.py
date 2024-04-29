from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class UserComplementationModelViewSet(ModelViewSet):
    serializer_class = serializers.UserComplementationSerializer
    queryset = models.UsuarioComplementacion.objects.all()

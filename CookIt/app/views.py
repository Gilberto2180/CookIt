from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from . import models, serializers

User = get_user_model()


class UserModelViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

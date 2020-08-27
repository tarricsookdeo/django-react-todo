from rest_framework.generics import ListAPIView

from . import models, serializers


class UserListView(ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

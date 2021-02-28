
from rest_framework import viewsets
from . import models
from . import serializer

class APIsViewsets(viewsets.ModelViewSet):
    queryset = models.HocTap.objects.all()
    serializer_class = serializer.HoctapSerializer
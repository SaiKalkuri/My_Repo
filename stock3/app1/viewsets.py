from rest_framework import viewsets
from app1.models import *
from app1.serializers import *

class CategoryModelViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
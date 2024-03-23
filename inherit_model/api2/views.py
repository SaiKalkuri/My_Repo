from rest_framework import viewsets
from .serializers import ProxyUserProfileSerializer
from api2.models import ProxyUserProfile

class ProxyUserProfileViewSet(viewsets.ModelViewSet):
    queryset=ProxyUserProfile.objects.all()
    serializer_class=ProxyUserProfileSerializer




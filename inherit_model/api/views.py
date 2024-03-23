from rest_framework import viewsets
from .serializers import UserProfileSerializer
# from django.contrib.auth.models import User
from api.models import UserProfile

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


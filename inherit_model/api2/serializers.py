from rest_framework import serializers 
from api2.models import ProxyUserProfile
class ProxyUserProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = ProxyUserProfile
        fields=["pan_card","mobile_no"]

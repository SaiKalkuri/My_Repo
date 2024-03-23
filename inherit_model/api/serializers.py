from rest_framework import serializers 
from api.models import UserProfile,User
class UserProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = UserProfile
        fields=["username","password","pan_card","mobile_no"]

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ["username", "password"]
from django.db import models
from django.contrib.auth.models import User



class UserProfile(User):
    pan_card=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100,default='')


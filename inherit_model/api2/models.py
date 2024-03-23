from django.db import models
from api.models import UserProfile

class ProxyUserProfile(UserProfile):
    class Meta:
        proxy = True
        ordering=['pan_card']


    







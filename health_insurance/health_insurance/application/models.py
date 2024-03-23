from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Common_fields(models.Model):
    created_by=models.ForeignKey(User, related_name="%(class)s_created_by",on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_by=models.ForeignKey(User, related_name="%(class)s_updated_by",on_delete=models.CASCADE,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        abstract = True

class Customer(Common_fields):
    customer_name=models.CharField(max_length=200)
    unique_number=models.CharField(max_length=250,unique=True)
    date_of_birth=models.DateField()
    phone_number=models.CharField(max_length=20)
    address=models.TextField()

class Premium(Common_fields):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    policy_number=models.CharField(max_length=50)
    premium_amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_date=models.DateField()

class Claims(Common_fields):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    claim_number=models.CharField(max_length=50)
    claim_date=models.DateField()
    claim_amount=models.DecimalField(max_digits=10,decimal_places=2)

class Expanses(Common_fields):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    








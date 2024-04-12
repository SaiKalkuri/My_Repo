from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    unique_num = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class OpeningStock(models.Model):
    opening_stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Sales(models.Model):
    stock = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class Purchase(models.Model):
    stock = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


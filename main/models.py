from django.db import models

# Create your models here.

from django.db import models

# tugas 2 : membuat suatu class produk dengan atribut name, price, amount, description
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()
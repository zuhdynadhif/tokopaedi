from django.db import models

# Create your models here.

from django.db import models
# ----------- tugas 4 -----------
from django.contrib.auth.models import User

# tugas 2 : membuat suatu class produk dengan atribut name, price, amount, description
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()
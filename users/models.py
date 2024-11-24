from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo  = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

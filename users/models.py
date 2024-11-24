from django.db import models
from projects.models import Project

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo  = models.CharField(max_length=200,unique=True)
    projects = models.ManyToManyField(Project, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
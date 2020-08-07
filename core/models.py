from django.db import models

# Create your models here.
class project(models.Model):
    nombre = models.CharField(max_length=200, default="user")
    mensaje = models.TextField()
    created = models.TimeField(auto_now_add=True)

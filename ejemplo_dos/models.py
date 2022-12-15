from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=4000)
    publicado_el = models.DateField()

# Create your models here.

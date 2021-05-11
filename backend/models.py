from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=32)

class Message(models.Model):
    message = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)  # campo de caracterirs, limite
    # text es un limitante como caracter pero de mas capacidad
    content = models.TextField()

from django.db import models

# Create your models here.

class New(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)
    autor = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)
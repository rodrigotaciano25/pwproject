from django.db import models

class New(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)
    autor = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.titulo[:50]
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    apelido = models.CharField(max_length=30)

    def __str__(self):
          return self.nome[:50]

class Cadeira(models.Model):
    nome = models.CharField(max_length=60)
    ano = models.IntegerField()
    link_cadeira = models.CharField(max_length=1000, default='1')
    semestre = models.IntegerField()
    descricao = models.TextField(max_length=1000)
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=20, default='1')
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default='1')
    docentes_praticas = models.ManyToManyField(Pessoa, related_name='professor_pratica')
    linguagens = models.CharField(max_length=40, default='1')

    def __str__(self):
        return self.nome[:50]
    
class Lab(models.Model):
    titulo = models.CharField(max_length=70)
    descricao = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self):
          return self.titulo[:50]
from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo

class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    livros = models.ManyToManyField(Livro, related_name="colecoes")
    colecionador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="colecoes")

    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"

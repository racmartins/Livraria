from django.db import models
from django.contrib.auth.models import User


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    data_publicacao = models.DateField()
    # Relacionamento com o modelo User
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

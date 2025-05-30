import os  # Adicione esta linha no início do arquivo
from django.db import models
from django.contrib.auth.models import User
from autores.models import Autor
from editoras.models import Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor, related_name='livros')
    editora = models.ForeignKey(
        Editora,
        on_delete=models.CASCADE,
        related_name='livros',
        null=True,
        blank=True
    )
    categoria = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    data_publicacao = models.DateField()
    data_atualizacao = models.DateTimeField(auto_now=True)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if self.id:
            try:
                old_livro = Livro.objects.get(id=self.id)
                if old_livro.capa and self.capa and old_livro.capa != self.capa:
                    if os.path.isfile(old_livro.capa.path):
                        os.remove(old_livro.capa.path)
            except Livro.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.capa:
            if os.path.isfile(self.capa.path):
                os.remove(self.capa.path)
        super().delete(*args, **kwargs)

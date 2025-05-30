from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.TextField()
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='editoras/', blank=True, null=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.nome

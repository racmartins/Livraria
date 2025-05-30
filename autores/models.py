from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255) # Nome do autor
    biografia = models.TextField(blank=True, null=True) # Biografia
    data_nascimento = models.DateField(blank=True, null=True) # Data de nascimento do autor
    foto = models.ImageField(upload_to='autores/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome # Exibe o nome do autor no painel de administração

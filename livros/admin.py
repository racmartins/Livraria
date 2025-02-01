from django.contrib import admin
from .models import Livro

admin.site.register(Livro)

# Personalize os textos do cabeçalho
admin.site.site_header = "BackOffice Livraria"
admin.site.site_title = "Administração da Livraria"
admin.site.index_title = "Bem Vindo ao painel Administrativo da Livraria"

from django.urls import path
from . import views

app_name = 'autores'  # Define o namespace

urlpatterns = [
    path('', views.lista_autores, name='lista_autores'),
    path('adicionar/', views.adicionar_autor, name='adicionar_autor'),
    path('<int:autor_id>/', views.detalhes_autor, name='detalhes_autor'),
    path('<int:autor_id>/editar/', views.editar_autor, name='editar_autor'),
    path('<int:autor_id>/excluir/', views.excluir_autor, name='excluir_autor'),
]

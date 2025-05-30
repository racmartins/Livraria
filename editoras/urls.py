from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_editoras, name='lista_editoras'),
    path('adicionar/', views.adicionar_editora, name='adicionar_editora'),
    path('<int:editora_id>/', views.detalhes_editora, name='detalhes_editora'),
    path('<int:editora_id>/editar/', views.editar_editora, name='editar_editora'),
    path('<int:editora_id>/excluir/',
         views.excluir_editora, name='excluir_editora'),
]

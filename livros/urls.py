from django.urls import path, include
from . import views

app_name = 'livros'  # Define o namespace do app

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.listar_livros, name='listar_livros'),
    path('<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    path('registar/', views.registar_livro, name='registar_livro'),
    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),
]

from django.urls import path, include
from . import views

app_name = 'livros'  # Define o namespace do app

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.listar_livros, name='listar_livros'),
    path('<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
]
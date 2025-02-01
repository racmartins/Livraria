from django.contrib import admin
from django.urls import path, include
from livros import views  # Importe a view

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel administrativo
    path('', views.index, name='index'),  # Rota para a página inicial
    path('livros/', include(('livros.urls', 'livros'),
         namespace='livros')),  # URLs do app livros
    # URLs de autenticação
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro

# View para a página inicial


def index(request):
    return render(request, 'index.html')

# View para listar os livros


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})

# View para detalhes de um livro


def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'livros/detalhes_livro.html', {'livro': livro})

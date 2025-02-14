from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Livro
from .forms import LivroForm

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

# View para registar um livro


@login_required
def registar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.utilizador = request.user  # Associar ao utilizador logado
            livro.save()
            return redirect('livros:listar_livros')  # Redirecionamento correto
    else:
        form = LivroForm()

    return render(request, 'livros/registar_livro.html', {'form': form})

# View para editar um livro


@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            # Correção no redirecionamento com namespace
            return redirect('livros:detalhes_livro', livro_id=livro.id)
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livros/editar_livro.html', {'form': form, 'livro': livro})

# View para excluir um livro


@login_required
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    livro.delete()
    return redirect('livros:listar_livros')  # Redirecionamento correto

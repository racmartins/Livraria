from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Livro
from .forms import LivroForm
from autores.models import Autor
from editoras.models import Editora


def index(request):
    # Obtém os dados para a página inicial
    context = {
        'total_livros': Livro.objects.count(),
        'total_autores': Autor.objects.count(),
        'total_editoras': Editora.objects.count(),
    }

    if request.user.is_authenticated:
        # Adiciona livros recentes apenas para utilizadores autenticados
        context['ultimos_livros'] = Livro.objects.all().order_by(
            '-data_publicacao')[:6]

    return render(request, 'index.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout realizado com sucesso!')
    return redirect('index')


@login_required
def listar_livros(request):
    # Obtém os parâmetros de busca
    search_query = request.GET.get('search', '')
    autor_id = request.GET.get('autor')
    editora_id = request.GET.get('editora')
    ordenacao = request.GET.get('ordem', '-data_publicacao')

    # Inicia o queryset
    livros = Livro.objects.all()

    # Aplica os filtros
    if search_query:
        livros = livros.filter(
            Q(titulo__icontains=search_query) |
            Q(autores__nome__icontains=search_query) |
            Q(isbn__icontains=search_query)
        ).distinct()

    if autor_id:
        livros = livros.filter(autores__id=autor_id)

    if editora_id:
        livros = livros.filter(editora_id=editora_id)

    # Ordenação
    ordem_permitida = {
        'titulo': 'titulo',
        '-titulo': '-titulo',
        'data': 'data_publicacao',
        '-data': '-data_publicacao',
        'preco': 'preco',
        '-preco': '-preco'
    }
    livros = livros.order_by(
        ordem_permitida.get(ordenacao, '-data_publicacao'))

    # Paginação
    items_por_pagina = int(request.GET.get('items', 12))
    paginator = Paginator(livros, items_por_pagina)
    page = request.GET.get('page')
    livros = paginator.get_page(page)

    # Obtém listas de autores e editoras para os filtros
    autores = Autor.objects.all().order_by('nome')
    editoras = Editora.objects.all().order_by('nome')

    context = {
        'livros': livros,
        'autores': autores,
        'editoras': editoras,
        'search_query': search_query,
        'selected_autor': autor_id,
        'selected_editora': editora_id,
        'ordenacao': ordenacao,
        'items_por_pagina': items_por_pagina
    }

    return render(request, 'livros/listar_livros.html', context)


@login_required
def registar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                livro = form.save(commit=False)
                livro.utilizador = request.user
                livro.save()
                form.save_m2m()
                messages.success(
                    request, f'✅ O livro "{livro.titulo}" foi registado com sucesso!')
                return redirect('livros:detalhes_livro', livro_id=livro.id)
            except Exception as e:
                messages.error(
                    request, f'❌ Erro ao registar o livro: {str(e)}')
    else:
        form = LivroForm()

    return render(request, 'livros/registar_livro.html', {
        'form': form,
        'titulo': 'Registar Novo Livro'
    })


@login_required
def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    pode_editar = request.user.is_staff or request.user == livro.utilizador

    context = {
        'livro': livro,
        'pode_editar': pode_editar,
        'livros_relacionados': Livro.objects.filter(
            Q(autores__in=livro.autores.all()) |
            Q(editora=livro.editora)
        ).exclude(id=livro.id).distinct()[:4]
    }

    return render(request, 'livros/detalhes_livro.html', context)


@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if livro.utilizador != request.user and not request.user.is_staff:
        messages.error(request, '❌ Não tem permissão para editar este livro.')
        return redirect('livros:detalhes_livro', livro_id=livro.id)

    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            # Se uma nova imagem foi enviada
            if 'capa' in request.FILES:
                # Se já existe uma imagem antiga, exclua-a
                if livro.capa:
                    import os
                    if os.path.isfile(livro.capa.path):
                        os.remove(livro.capa.path)

            livro = form.save()
            messages.success(
                request, f'✅ O livro "{livro.titulo}" foi atualizado com sucesso!')
            return redirect('livros:detalhes_livro', livro_id=livro.id)
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livros/editar_livro.html', {
        'form': form,
        'livro': livro
    })


@login_required
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    # Verifica se o utilizador tem permissão para excluir
    if livro.utilizador != request.user and not request.user.is_staff:
        messages.error(request, 'Não tem permissão para excluir este livro.')
        return redirect('livros:detalhes_livro', livro_id=livro.id)

    if request.method == 'POST':
        try:
            titulo = livro.titulo
            livro.delete()
            messages.success(
                request, f'🗑️ O livro "{titulo}" foi excluído com sucesso!')
            return redirect('livros:listar_livros')
        except Exception as e:
            messages.error(request, f'Erro ao excluir livro: {str(e)}')
            return redirect('livros:detalhes_livro', livro_id=livro.id)

    return render(request, 'livros/confirmar_exclusao.html', {'livro': livro})

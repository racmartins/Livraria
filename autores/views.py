from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Autor
from .forms import AutorForm


def lista_autores(request):
    autores = Autor.objects.all().order_by('nome')
    return render(request, 'autores/lista_autores.html', {'autores': autores})


@login_required
def adicionar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            autor = form.save()
            messages.success(request, 'Autor adicionado com sucesso!')
            return redirect('autores:detalhes_autor', autor_id=autor.id)
    else:
        form = AutorForm()
    return render(request, 'autores/form_autor.html', {'form': form})


def detalhes_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    return render(request, 'autores/detalhes_autor.html', {'autor': autor})


@login_required
def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor atualizado com sucesso!')
            return redirect('autores:detalhes_autor', autor_id=autor.id)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autores/form_autor.html', {'form': form, 'autor': autor})


@login_required
def excluir_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor excluído com sucesso!')
        return redirect('autores:lista_autores')
    return redirect('autores:detalhes_autor', autor_id=autor.id)

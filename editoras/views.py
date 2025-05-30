from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Editora
from .forms import EditoraForm


def lista_editoras(request):
    editoras = Editora.objects.all().order_by('nome')
    return render(request, 'editoras/lista_editoras.html', {'editoras': editoras})


def detalhes_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    return render(request, 'editoras/detalhes_editora.html', {'editora': editora})


@login_required
def adicionar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST, request.FILES)
        if form.is_valid():
            editora = form.save()
            messages.success(request, 'Editora adicionada com sucesso!')
            return redirect('editoras:detalhes_editora', editora_id=editora.id)
    else:
        form = EditoraForm()
    return render(request, 'editoras/form_editora.html', {
        'form': form,
        'titulo': 'Adicionar Editora'
    })


@login_required
def editar_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, request.FILES, instance=editora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora atualizada com sucesso!')
            return redirect('editoras:detalhes_editora', editora_id=editora.id)
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'editoras/form_editora.html', {
        'form': form,
        'titulo': 'Editar Editora',
        'editora': editora
    })


@login_required
def excluir_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    if request.method == 'POST':
        editora.delete()
        messages.success(request, 'Editora excluída com sucesso!')
        return redirect('editoras:lista_editoras')
    return redirect('editoras:detalhes_editora', editora_id=editora.id)

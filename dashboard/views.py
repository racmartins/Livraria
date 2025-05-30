from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from livros.models import Livro
from autores.models import Autor
from editoras.models import Editora


def is_admin(user):
    return user.is_staff


@login_required
# Adicione esta linha para garantir que apenas admin pode acessar
@user_passes_test(is_admin)
def dashboard(request):  # Mantém o nome original da sua função
    # Estatísticas gerais
    total_livros = Livro.objects.count()
    total_autores = Autor.objects.count()
    total_editoras = Editora.objects.count()

    # Livros por mês (últimos 6 meses)
    livros_por_mes = Livro.objects.annotate(
        month=TruncMonth('data_publicacao')
    ).values('month').annotate(
        total=Count('id')
    ).order_by('-month')[:6]

    # Top autores
    top_autores = Autor.objects.annotate(
        num_livros=Count('livros')
    ).order_by('-num_livros')[:5]

    # Top editoras
    top_editoras = Editora.objects.annotate(
        num_livros=Count('livros')
    ).order_by('-num_livros')[:5]

    context = {
        'total_livros': total_livros,
        'total_autores': total_autores,
        'total_editoras': total_editoras,
        'livros_por_mes': livros_por_mes,
        'top_autores': top_autores,
        'top_editoras': top_editoras,
    }

    # Alterado para admin_dashboard.html
    return render(request, 'dashboard/admin_dashboard.html', context)

from django.contrib import admin
from .models import Editora


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'website')
    list_filter = ('nome',)
    search_fields = ('nome', 'email', 'telefone')
    ordering = ('nome',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'logo')
        }),
        ('Contato', {
            'fields': ('email', 'telefone', 'website')
        }),
        ('Endereço', {
            'fields': ('endereco',)
        }),
    )

    # Opcional: Adicionar ações personalizadas
    actions = ['marcar_como_ativa']

    def marcar_como_ativa(self, request, queryset):
        queryset.update(ativa=True)
    marcar_como_ativa.short_description = "Marcar editoras selecionadas como ativas"

from django.contrib import admin
from django.contrib.admin import AdminSite


class LivrariaAdminSite(AdminSite):
    site_header = 'Livraria Online'
    site_title = 'Administração da Livraria'
    index_title = 'Painel de Controlo'

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Reordena as aplicações
        app_ordering = {
            'livros': 1,
            'autores': 2,
            'editoras': 3,
            'auth': 4,
        }
        app_list.sort(key=lambda x: app_ordering.get(x['app_label'], 10))
        return app_list


admin_site = LivrariaAdminSite(name='admin')

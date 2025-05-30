from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from livros import views
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('livros/', include(('livros.urls', 'livros'), namespace='livros')),
    path('autores/', include(('autores.urls', 'autores'), namespace='autores')),
    path('editoras/', include(('editoras.urls', 'editoras'), namespace='editoras')),

    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    # Dashboard - usando o nome da sua função original
    path('dashboard/', dashboard_views.dashboard, name='admin_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

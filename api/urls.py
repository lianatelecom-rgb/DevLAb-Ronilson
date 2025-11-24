from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import (
    home,
    projeto_detalhe,
    UsuarioViewSet,
    ProjetoViewSet,
    EquipeViewSet,
    ParticipacaoProjetoViewSet,
    MembrosEquipeViewSet,
    UsuarioProjetosView,
    ProjetoEquipesView,
    UsuarioVisaoGeralView
)

# ------------------ Roteamento da API ------------------
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'projetos', ProjetoViewSet, basename='projeto')
router.register(r'equipes', EquipeViewSet, basename='equipe')
router.register(r'participacoes', ParticipacaoProjetoViewSet, basename='participacao')
router.register(r'membros-equipe', MembrosEquipeViewSet, basename='membros-equipe')

# ------------------ URLs do app ------------------
urlpatterns = [
    # Site
    path('', home, name='home'),
    path('projeto/<int:pk>/', projeto_detalhe, name='projeto-detalhe'),  # detalhe do projeto
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # API
    path('api/', include(router.urls)),

    # Rotas de relacionamento
    path('api/usuarios/<int:pk>/projetos/', UsuarioProjetosView.as_view(), name='usuario-projetos'),
    path('api/projetos/<int:pk>/equipes/', ProjetoEquipesView.as_view(), name='projeto-equipes'),
    path('api/usuarios/<int:pk>/visao-geral/', UsuarioVisaoGeralView.as_view(), name='usuario-visao-geral'),
]

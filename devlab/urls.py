from django.contrib import admin
from django.urls import path
from api_usuarios import views as usuarios_views
from api_projetos import views as projetos_views
from api_equipes import views as equipe_views  # Certo: api_equipes

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login / Logout
    path('', usuarios_views.login_view, name='login'),
    path('logout/', usuarios_views.logout_view, name='logout'),

    # Home por tipo de usuário
    path('home/coordenador/', projetos_views.home_coordenador, name='home_coordenador'),
    path('home/professor/', projetos_views.home_professor, name='home_professor'),
    path('home/estudante/', projetos_views.home_estudante, name='home_estudante'),

    # PERFIL
    path('editar-perfil/', usuarios_views.editar_perfil, name='editar_perfil'),
    path('ver-perfil/', usuarios_views.ver_perfil, name='ver_perfil'),

    # Criar Projeto / Equipe / Usuário (somente coordenador)
    path('projetos/criar/', projetos_views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:pk>/editar/', projetos_views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/deletar/', projetos_views.deletar_projeto, name='deletar_projeto'),

    path('equipes/criar/', equipe_views.criar_equipe, name='criar_equipe'),
    path('equipes/<int:equipe_id>/editar/', equipe_views.editar_equipe, name='editar_equipe'),
    
    # Comentado: view ainda não criada, evita erro
    # path('equipes/<int:equipe_id>/deletar/', equipe_views.deletar_equipe, name='deletar_equipe'),

    path('usuarios/criar/', usuarios_views.criar_usuario, name='criar_usuario'),

    # Detalhes
    path('projetos/<int:pk>/', projetos_views.detalhe_projeto, name='detalhe_projeto'),
    path('equipes/<int:equipe_id>/', equipe_views.detalhe_equipe, name='detalhe_equipe'),
]

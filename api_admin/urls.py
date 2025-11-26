from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_admin.views import UsuarioViewSet, ProjetoViewSet, EquipeViewSet, ParticipacaoProjetoViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'equipes', EquipeViewSet)
router.register(r'participacoes', ParticipacaoProjetoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

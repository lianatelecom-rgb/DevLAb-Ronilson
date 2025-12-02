from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet, ParticipacaoProjetoViewSet

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'participacoes', ParticipacaoProjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

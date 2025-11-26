from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet, EquipeViewSet

router = DefaultRouter()
router.register(r'projeto', ProjetoViewSet, basename='projeto')
router.register(r'equipe', EquipeViewSet, basename='equipe')

urlpatterns = router.urls

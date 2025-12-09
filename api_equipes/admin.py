from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Equipe


def usuario_tem_permissao(request):
    """Verifica se o usuário está no grupo professor ou coordenador."""
    return (
        request.user.is_superuser or
        request.user.groups.filter(name__in=['professor', 'coordenador']).exists()
    )


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'criado_em')
    search_fields = ('nome',)
    list_filter = ('criado_em',)
    ordering = ('id',)

    # Bloqueia adicionar equipe para quem não é professor/coordenador
    def has_add_permission(self, request):
        return usuario_tem_permissao(request)

    # Bloqueia edição
    def has_change_permission(self, request, obj=None):
        return usuario_tem_permissao(request)

    # Bloqueia remoção
    def has_delete_permission(self, request, obj=None):
        return usuario_tem_permissao(request)

    # Bloqueia visualização
    def has_view_permission(self, request, obj=None):
        return usuario_tem_permissao(request)


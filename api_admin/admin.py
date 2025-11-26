from django.contrib import admin
from api_projetos.models import Projeto, Equipe, ParticipacaoProjeto
from api_aluno.models import Usuario

# ========================
# Admin para Projetos
# ========================
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status', 'data_inicio', 'data_fim_prevista')
    search_fields = ('titulo', 'cliente')
    list_filter = ('status',)
    # filter_horizontal removido porque 'participantes' usa 'through'


# ========================
# Admin para Equipes
# ========================
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'projeto', 'lider')
    search_fields = ('nome',)
    list_filter = ('projeto',)


# ========================
# Admin para Participação de Projetos
# ========================
@admin.register(ParticipacaoProjeto)
class ParticipacaoProjetoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'projeto', 'papel')
    search_fields = ('usuario__username', 'projeto__titulo')


# ========================
# Admin para Usuários
# ========================
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    # filter_horizontal removido para evitar erros

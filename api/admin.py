from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario, Projeto, Equipe, ParticipacaoProjeto, MembrosEquipe
from django.utils.translation import gettext_lazy as _


class UsuarioAdmin(BaseUserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'curso', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'curso')}),
        (_('Permissões'), {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        (_('Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'curso', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Projeto)
admin.site.register(Equipe)
admin.site.register(ParticipacaoProjeto)
admin.site.register(MembrosEquipe)

# api_usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'tipo', 'curso', 'matricula', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo', 'telefone', 'curso', 'matricula')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo', 'telefone', 'curso', 'matricula')}),
    )

admin.site.register(Usuario, UsuarioAdmin)

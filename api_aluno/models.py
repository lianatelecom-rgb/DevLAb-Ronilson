# api_aluno/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    curso = models.CharField(max_length=100, blank=True, null=True)
    is_lider = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username

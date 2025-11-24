# api/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# ----------- Usuário -----------
class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('coordenador', 'Coordenador'),
    )
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    curso = models.CharField(max_length=100, blank=True, null=True)
    matricula = models.CharField(max_length=50, blank=True, null=True)

    # Corrigindo conflitos com grupos e permissões do Django
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_custom',
        blank=True,
        help_text='Grupos que este usuário pertence.',
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_custom',
        blank=True,
        help_text='Permissões específicas deste usuário.',
        verbose_name='permissões do usuário'
    )

    def __str__(self):
        return self.username


# ----------- Projeto -----------
class Projeto(models.Model):
    STATUS_CHOICES = (
        ('planejamento', 'Planejamento'),
        ('andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    cliente = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    data_inicio = models.DateField()
    data_fim_prevista = models.DateField()

    def __str__(self):
        return self.titulo


# ----------- Equipe -----------
class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='equipes')
    lider = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='liderancas')

    def __str__(self):
        return self.nome


# ----------- Participação em Projeto -----------
class ParticipacaoProjeto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='projetos_participando')
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='participantes')

    class Meta:
        unique_together = ('usuario', 'projeto')  # Evita duplicação

    def __str__(self):
        return f"{self.usuario} em {self.projeto}"


# ----------- Membros da Equipe -----------
class MembrosEquipe(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='equipes')
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='membros')

    class Meta:
        unique_together = ('usuario', 'equipe')  # Evita duplicação

    def __str__(self):
        return f"{self.usuario} na {self.equipe}"

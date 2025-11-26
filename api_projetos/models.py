from django.db import models
from api_aluno.models import Usuario

class Projeto(models.Model):
    STATUS_CHOICES = (
        ('planejado', 'Planejado'),
        ('andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    cliente = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,  # permite que registros antigos fiquem sem cliente
        blank=True,
        related_name='projetos_cliente'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejado')
    data_inicio = models.DateField(null=True, blank=True)
    data_fim_prevista = models.DateField(null=True, blank=True)

    participantes = models.ManyToManyField(
        Usuario,
        through='ParticipacaoProjeto',
        related_name='projetos'
    )

    def __str__(self):
        return self.titulo

class ParticipacaoProjeto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    papel = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('usuario', 'projeto')

    def __str__(self):
        return f"{self.usuario.username} no projeto {self.projeto.titulo}"

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='equipes')
    membros = models.ManyToManyField(Usuario, related_name='equipes')
    lider = models.OneToOneField(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lider_equipe'
    )

    def __str__(self):
        return f"{self.nome} ({self.projeto.titulo})"

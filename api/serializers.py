from rest_framework import serializers
from .models import Usuario, Projeto, Equipe, ParticipacaoProjeto, MembrosEquipe

# -------------------- Usuario --------------------
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tipo_usuario', 'curso', 'matricula']

# -------------------- Projeto --------------------
class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'titulo', 'descricao', 'cliente', 'status', 'data_inicio', 'data_fim_prevista']

# -------------------- Equipe --------------------
class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome', 'descricao', 'projeto', 'lider']

# -------------------- ParticipacaoProjeto --------------------
class ParticipacaoProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipacaoProjeto
        fields = ['id', 'usuario', 'projeto']

# -------------------- MembrosEquipe --------------------
class MembrosEquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembrosEquipe
        fields = ['id', 'usuario', 'equipe']

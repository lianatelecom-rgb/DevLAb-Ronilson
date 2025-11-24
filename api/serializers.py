from rest_framework import serializers
from .models import Usuario, Projeto, Equipe, ParticipacaoProjeto, MembrosEquipe


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tipo_usuario', 'curso', 'matricula']


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'titulo', 'descricao', 'cliente', 'status', 'data_inicio', 'data_fim_prevista']


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome', 'descricao', 'projeto', 'lider']


class ParticipacaoProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipacaoProjeto
        fields = ['id', 'usuario', 'projeto']


class MembrosEquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembrosEquipe
        fields = ['id', 'usuario', 'equipe']

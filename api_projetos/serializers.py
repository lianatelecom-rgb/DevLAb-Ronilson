from rest_framework import serializers
from .models import Projeto, ParticipacaoProjeto
from api_usuarios.models import Usuario
from api_usuarios.serializers import UsuarioSerializer

class ParticipacaoProjetoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), source='usuario', write_only=True
    )

    class Meta:
        model = ParticipacaoProjeto
        fields = ['id', 'usuario', 'usuario_id', 'papel', 'projeto']

class ProjetoSerializer(serializers.ModelSerializer):
    participantes = UsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = [
            'id',
            'titulo',
            'descricao',
            'cliente',
            'status',
            'data_inicio',
            'data_fim_prevista',
            'participantes'
        ]

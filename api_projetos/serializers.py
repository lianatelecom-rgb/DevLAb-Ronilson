from rest_framework import serializers
from .models import Projeto, Equipe

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'titulo', 'descricao', 'status']

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome', 'lider', 'projeto']

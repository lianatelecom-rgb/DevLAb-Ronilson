from rest_framework import viewsets, permissions, serializers
from api_aluno.models import Usuario
from api_projetos.models import Projeto, Equipe, ParticipacaoProjeto

# Permissão: apenas admins
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_superuser

# Serializers
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class ParticipacaoProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipacaoProjeto
        fields = '__all__'

# ViewSets
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [IsAdminUser]

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAdminUser]

class ParticipacaoProjetoViewSet(viewsets.ModelViewSet):
    queryset = ParticipacaoProjeto.objects.all()
    serializer_class = ParticipacaoProjetoSerializer
    permission_classes = [IsAdminUser]

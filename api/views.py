from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Usuario, Projeto, Equipe, ParticipacaoProjeto, MembrosEquipe
from .serializers import UsuarioSerializer, ProjetoSerializer, EquipeSerializer, ParticipacaoProjetoSerializer, MembrosEquipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    usuarios = Usuario.objects.all()
    projetos = Projeto.objects.all()
    equipes = Equipe.objects.all()

    context = {
        'usuarios': usuarios,
        'projetos': projetos,
        'equipes': equipes
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def projeto_detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    equipes = Equipe.objects.filter(projeto=projeto)
    context = {
        'projeto': projeto,
        'equipes': equipes,
    }
    return render(request, 'projeto_detalhe.html', context)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class ParticipacaoProjetoViewSet(viewsets.ModelViewSet):
    queryset = ParticipacaoProjeto.objects.all()
    serializer_class = ParticipacaoProjetoSerializer

class MembrosEquipeViewSet(viewsets.ModelViewSet):
    queryset = MembrosEquipe.objects.all()
    serializer_class = MembrosEquipeSerializer


class UsuarioProjetosView(APIView):
    def get(self, request, pk):
        projetos = Projeto.objects.filter(participacaoprojeto__usuario_id=pk)
        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data)

class ProjetoEquipesView(APIView):
    def get(self, request, pk):
        equipes = Equipe.objects.filter(projeto_id=pk)
        serializer = EquipeSerializer(equipes, many=True)
        return Response(serializer.data)

class UsuarioVisaoGeralView(APIView):
    def get(self, request, pk):
        usuario = Usuario.objects.get(id=pk)
        data = {
            "usuario": usuario.nome,
            "projetos": [p.nome for p in usuario.projetos.all()],
            "lider": usuario.is_lider  
        }
        return Response(data)

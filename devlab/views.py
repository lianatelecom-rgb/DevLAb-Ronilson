from django.shortcuts import render
from api_projetos.models import Projeto
from api_aluno.models import Usuario

def home(request):
    query = request.GET.get('q', '').strip()  # remove espaços desnecessários

    if query:
        projetos = Projeto.objects.filter(titulo__icontains=query)
        usuarios = Usuario.objects.filter(username__icontains=query)
    else:
        projetos = Projeto.objects.all()
        usuarios = Usuario.objects.all()

    context = {
        'projetos': projetos,
        'usuarios': usuarios,
        'query': query,  # útil para manter o valor da busca na input
    }

    return render(request, 'home.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Equipe, ParticipacaoEquipe
from api_projetos.models import Projeto
from api_usuarios.models import Usuario
from .forms import EquipeForm  # <- Importa o form que já existe

# =========================
# Criar equipe
# =========================
@login_required
def criar_equipe(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_coordenador')
    else:
        form = EquipeForm()

    return render(request, 'criar_equipe.html', {'form': form})

# =========================
# Detalhe equipe
# =========================
@login_required
def detalhe_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    participacoes = ParticipacaoEquipe.objects.filter(equipe=equipe)
    return render(request, 'detalhe_equipe.html', {'equipe': equipe, 'participacoes': participacoes})

# =========================
# Editar equipe
# =========================
@login_required
def editar_equipe(request, equipe_id):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    equipe = get_object_or_404(Equipe, id=equipe_id)

    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('home_coordenador')
    else:
        form = EquipeForm(instance=equipe)

    return render(request, 'editar_equipe.html', {'form': form, 'equipe': equipe})

# =========================
# Deletar equipe
# =========================
@login_required
def deletar_equipe(request, equipe_id):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    equipe = get_object_or_404(Equipe, id=equipe_id)

    if request.method == 'POST':
        equipe.delete()
        return redirect('home_coordenador')

    return render(request, 'deletar_equipe.html', {'equipe': equipe})

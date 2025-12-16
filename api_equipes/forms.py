from django import forms
from .models import Equipe
from api_projetos.models import Projeto
from api_usuarios.models import Usuario

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'projeto', 'lider']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mostrar apenas os projetos existentes
        self.fields['projeto'].queryset = Projeto.objects.all()
        # Mostrar apenas usuários tipo estudante como líder
        self.fields['lider'].queryset = Usuario.objects.filter(tipo='estudante')
        # Adicionar labels bonitos (opcional)
        self.fields['nome'].label = "Nome da Equipe"
        self.fields['descricao'].label = "Descrição"
        self.fields['projeto'].label = "Projeto"
        self.fields['lider'].label = "Líder da Equipe"

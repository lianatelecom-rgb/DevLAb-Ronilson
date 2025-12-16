from django import forms
from .models import Projeto
from api_usuarios.models import Usuario

class ProjetoForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(
        queryset=Usuario.objects.filter(tipo='estudante'),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Estudantes Participantes"
    )

    class Meta:
        model = Projeto
        fields = ['titulo', 'cliente', 'status', 'professor_responsavel', 'participantes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apenas professores na lista de professor_responsavel
        self.fields['professor_responsavel'].queryset = Usuario.objects.filter(tipo='professor')

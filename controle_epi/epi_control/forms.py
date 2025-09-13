# epi_control/forms.py

from django import forms
from .models import Colaborador, Equipamento, Emprestimo
from django.utils import timezone

# Este formulário você já tem
class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo','cargo'] # Adicione outros campos como 'cpf', 'funcao' se os tiver no model

# 2. Formulário para Equipamentos
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome_equipamento', 'descricao', 'data_aquisicao'] # Campos do seu model Equipamento
        widgets = {
            'data_aquisicao': forms.DateInput(attrs={'type': 'date'}) # Widget para facilitar a seleção de data
        }    

# 3. Formulário para o Controle de EPI (Empréstimo)
class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        # Os campos que aparecerão no formulário de cadastro inicial
        fields = ['colaborador', 'equipamento', 'data_prevista_devolucao', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Requisito: Ocultar status "Devolvido", "Danificado" e "Perdido" no cadastro 
        self.fields['status'].choices = [
            ('Emprestado', 'Emprestado'),
            ('Em Uso', 'Em Uso'),
            ('Fornecido', 'Fornecido'),
        ]
        # Adicionar um widget para facilitar a seleção de data e hora
        self.fields['data_prevista_devolucao'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        )

    # Requisito: Validar se a data de devolução é no futuro 
    def clean_data_prevista_devolucao(self):
        data = self.cleaned_data.get('data_prevista_devolucao')
        if data and data < timezone.now():
            raise forms.ValidationError("A data prevista para devolução não pode ser no passado.")
        return data
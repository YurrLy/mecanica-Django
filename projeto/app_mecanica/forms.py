from django import forms
from .models import Veiculo, Peca, Cliente, Servico, Mecanico, Equipe, OrdemDeServico

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'placa', 'descricao', 'cliente']

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['tipo', 'valor']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['descricao', 'valor']

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['nome', 'endereco', 'especialidade']

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'membros']

class OrdemDeServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = ['veiculo', 'equipe', 'data_emissao', 'valor_total', 'data_conclusao']
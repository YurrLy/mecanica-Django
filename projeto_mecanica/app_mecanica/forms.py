from django import forms
from .models import Veiculo, Peca, Cliente, Servico

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

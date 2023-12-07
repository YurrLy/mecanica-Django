from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Veiculo, Peca, Cliente, Servico, OrdemDeServico
from .forms import VeiculoForm, PecaForm, ClienteForm, ServicoForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login bem-sucedido!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')

    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')


def veiculos_list(request):
    clientes = Cliente.objects.all()
    veiculos = Veiculo.objects.all()
    pecas = Peca.objects.all()
    servicos = Servico.objects.all()

    return render(request, 'veiculos_list.html', {
        'clientes': clientes,
        'veiculos': veiculos,
        'pecas': pecas,
        'servicos': servicos,
    })
    
def cadastrar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos_list')
    else:
        form = VeiculoForm()

    return render(request, 'cadastrar_veiculo.html', {'form': form})

def deletar_veiculo(request, veiculo_id):
    veiculo = Veiculo.objects.get(pk=veiculo_id)
    veiculo.delete()
    return redirect('veiculos_list')


def cadastrar_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos_list')
    else:
        form = PecaForm()

    return render(request, 'cadastrar_peca.html', {'form': form})

def deletar_peca(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)

    if request.method == 'POST':
        peca.delete()
        return redirect('veiculos_list') 

    return render(request, 'veiculos_list.html', {'peca': peca})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos_list')
    else:
        form = ClienteForm()

    return render(request, 'cadastrar_cliente.html', {'form': form})

def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    return redirect('veiculos_list')

def cadastrar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.save()

            return redirect('veiculos_list')
    else:
        form = ServicoForm()

    return render(request, 'cadastrar_servico.html', {'form': form})

def deletar_servico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    servico.delete()
    return redirect('veiculos_list')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Veiculo, Peca, Cliente, Servico, OrdemDeServico, Mecanico, Equipe
from .forms import VeiculoForm, PecaForm, ClienteForm, ServicoForm, MecanicoForm, EquipeForm, OrdemDeServicoForm


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

def listar_mecanicos(request):
    equipes = Equipe.objects.all()
    mecanicos = Mecanico.objects.all()
    return render(request, 'listar_mecanicos.html', {'mecanicos': mecanicos, 'equipes': equipes})

def cadastrar_mecanico(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mecanicos')
    else:
        form = MecanicoForm()

    return render(request, 'cadastrar_mecanico.html', {'form': form})

def cadastrar_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mecanicos')
    else:
        form = EquipeForm()

    return render(request, 'cadastrar_equipe.html', {'form': form})

def deletar_mecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
    mecanico.delete()
    return redirect('listar_mecanicos')

def deletar_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    equipe.delete()
    return redirect('listar_mecanicos')

def ordens_servico(request):
    ordens = OrdemDeServico.objects.all()
    return render(request, 'ordens_servico.html', {'ordens': ordens})

def cadastrar_ordem_servico(request):
    if request.method == 'POST':
        form = OrdemDeServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordens_servico')
    else:
        form = OrdemDeServicoForm()

    return render(request, 'cadastrar_ordem_servico.html', {'form': form})

def deletar_ordem_servico(request, ordem_id):
    ordem = get_object_or_404(OrdemDeServico, pk=ordem_id)
    ordem.delete()
    return redirect('ordens_servico')
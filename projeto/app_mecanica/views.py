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
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos_list.html', {'veiculos': veiculos})

def pecas_list(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas_list.html', {'pecas': pecas})

def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_list.html', {'clientes': clientes})

def servicos_list(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos_list.html', {'servicos': servicos})
    
def cadastrar_veiculo(request, veiculo_id=None):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id) if veiculo_id else None

    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculos_list')
    else:
        form = VeiculoForm(instance=veiculo)

    return render(request, 'cadastrar_veiculo.html', {'form': form, 'veiculo': veiculo})

def deletar_veiculo(request, veiculo_id):
    veiculo = Veiculo.objects.get(pk=veiculo_id)
    veiculo.delete()
    return redirect('veiculos_list')

def cadastrar_peca(request, peca_id=None):
    peca = get_object_or_404(Peca, pk=peca_id) if peca_id else None

    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('pecas_list')
    else:
        form = PecaForm(instance=peca)

    return render(request, 'cadastrar_peca.html', {'form': form, 'peca': peca})

def deletar_peca(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)

    if request.method == 'POST':
        peca.delete()
        return redirect('pecas_list') 

    return render(request, 'pecas_list.html', {'peca': peca})

def cadastrar_cliente(request, cliente_id=None):
    cliente = get_object_or_404(Cliente, id=cliente_id) if cliente_id else None

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado/editado com sucesso!')
            return redirect('clientes_list')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'cadastrar_cliente.html', {'form': form, 'cliente': cliente})

def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    return redirect('clientes_list')

def cadastrar_servico(request, servico_id=None):
    if servico_id:
        servico = get_object_or_404(Servico, pk=servico_id)
    else:
        servico = None

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servicos_list')
    else:
        form = ServicoForm(instance=servico)

    return render(request, 'cadastrar_servico.html', {'form': form, 'servico': servico})

def deletar_servico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    servico.delete()
    return redirect('servicos_list')

def listar_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'listar_mecanicos.html', {'mecanicos': mecanicos})

def listar_equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'listar_equipes.html', {'equipes': equipes})

def cadastrar_mecanico(request, mecanico_id=None):
    if mecanico_id:
        mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
    else:
        mecanico = None

    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('listar_mecanicos')
    else:
        form = MecanicoForm(instance=mecanico)

    return render(request, 'cadastrar_mecanico.html', {'form': form, 'mecanico': mecanico})

def cadastrar_equipe(request, equipe_id=None):
    if equipe_id:
        equipe = get_object_or_404(Equipe, pk=equipe_id)
    else:
        equipe = None

    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('listar_equipes')
    else:
        form = EquipeForm(instance=equipe)

    return render(request, 'cadastrar_equipe.html', {'form': form, 'equipe': equipe})

def deletar_mecanico(request, mecanico_id):
    mecanico = get_object_or_404(Mecanico, pk=mecanico_id)
    mecanico.delete()
    return redirect('listar_mecanicos')

def deletar_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    equipe.delete()
    return redirect('listar_equipes')

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
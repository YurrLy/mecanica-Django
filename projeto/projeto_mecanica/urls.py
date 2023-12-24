from django.urls import path
from app_mecanica.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('home/', home, name='home'),
    path('veiculos/', veiculos_list, name='veiculos_list'),
    path('veiculos/cadastrar/', cadastrar_veiculo, name='cadastrar_veiculo'),
    path('veiculos/deletar/<int:veiculo_id>/', deletar_veiculo, name='deletar_veiculo'),
    path('pecas/', pecas_list, name='pecas_list'),  # Adicionado
    path('pecas/cadastrar/', cadastrar_peca, name='cadastrar_peca'),
    path('pecas/deletar/<int:peca_id>/', deletar_peca, name='deletar_peca'),
    path('clientes/', clientes_list, name='clientes_list'),
    path('clientes/cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/deletar/<int:cliente_id>/', deletar_cliente, name='deletar_cliente'),
    path('servicos/', servicos_list, name='servicos_list'),
    path('servicos/cadastrar/', cadastrar_servico, name='cadastrar_servico'),
    path('servicos/deletar/<int:servico_id>/', deletar_servico, name='deletar_servico'),
    path('mecanicos/', listar_mecanicos, name='listar_mecanicos'),
    path('mecanicos/cadastrar/', cadastrar_mecanico, name='cadastrar_mecanico'),
    path('equipes/', listar_equipes, name='listar_equipes'),
    path('equipes/cadastrar/', cadastrar_equipe, name='cadastrar_equipe'),
    path('mecanicos/deletar/<int:mecanico_id>/', deletar_mecanico, name='deletar_mecanico'),
    path('equipes/deletar/<int:equipe_id>/', deletar_equipe, name='deletar_equipe'),
    path('ordens_servico/', ordens_servico, name='ordens_servico'),
    path('ordens_servico/cadastrar/', cadastrar_ordem_servico, name='cadastrar_ordem_servico'),
    path('ordens_servico/deletar/<int:ordem_id>/', deletar_ordem_servico, name='deletar_ordem_servico'),

]

from django.urls import path
from app_mecanica.views import login_view, home, veiculos_list, cadastrar_veiculo, deletar_veiculo, cadastrar_peca, deletar_peca, cadastrar_cliente, deletar_cliente, cadastrar_servico, deletar_servico

urlpatterns = [
    path('', login_view, name='login_view'),
    path('home/', home, name='home'),
    path('veiculos/', veiculos_list, name='veiculos_list'),
    path('veiculos/cadastrar/', cadastrar_veiculo, name='cadastrar_veiculo'),
    path('veiculos/deletar/<int:veiculo_id>/', deletar_veiculo, name='deletar_veiculo'),
    path('pecas/cadastrar/', cadastrar_peca, name='cadastrar_peca'),
    path('pecas/deletar/<int:peca_id>/', deletar_peca, name='deletar_peca'),
    path('clientes/cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/deletar/<int:cliente_id>/', deletar_cliente, name='deletar_cliente'),
    path('servicos/cadastrar/', cadastrar_servico, name='cadastrar_servico'),
    path('servicos/deletar/<int:servico_id>/', deletar_servico, name='deletar_servico'),

]

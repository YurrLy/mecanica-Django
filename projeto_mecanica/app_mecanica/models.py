from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=20)
    descricao = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)


class Mecanico(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=100)

class Equipe(models.Model):
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)

class OrdemDeServico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    data_emissao = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_conclusao = models.DateField()

class Servico(models.Model):
    ordem_de_servico = models.ForeignKey(OrdemDeServico, on_delete=models.CASCADE, null=True)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Peca(models.Model):
    ordem_de_servico = models.ForeignKey(OrdemDeServico, on_delete=models.CASCADE, null=True)
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=255)


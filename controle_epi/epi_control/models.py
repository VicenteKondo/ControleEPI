from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=50, blank=True)
    # Adicione outros campos que achar necessário, como CPF, função, etc.

    def __str__(self):
        return self.nome_completo

class Equipamento(models.Model):
    nome_equipamento = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição", blank=True, null=True)
 
    def __str__(self):
        return self.nome_equipamento

class Emprestimo(models.Model):
    # Definindo as opções para o campo 'status'
    STATUS_CHOICES = [
        ('Emprestado', 'Emprestado'),
        ('Em Uso', 'Em Uso'),
        ('Fornecido', 'Fornecido'),
        ('Devolvido', 'Devolvido'),
        ('Danificado', 'Danificado'),
        ('Perdido', 'Perdido'),
    ]

    # [cite_start]Relacionamentos com as outras tabelas usando Chave Estrangeira (ForeignKey) [cite: 38]
    colaborador = models.ForeignKey(
        'Colaborador',
        on_delete=models.CASCADE,  # Altere para CASCADE ou SET_NULL
        verbose_name="Colaborador"
    )
    equipamento = models.ForeignKey(
        'Equipamento',
        on_delete=models.CASCADE,
        verbose_name="Equipamento"
    )
    data_entrega = models.DateTimeField(default=timezone.now)
    data_prevista_devolucao = models.DateTimeField()
    data_efetiva_devolucao = models.DateTimeField(null=True, blank=True) # Pode ser nulo no início
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Emprestado')
    
    observacao_devolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipamento.nome_equipamento} para {self.colaborador.nome_completo}"

class ControleEPI(models.Model):
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('em_uso', 'Em Uso'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    colaborador = models.ForeignKey('Colaborador', on_delete=models.CASCADE, verbose_name="Colaborador")
    equipamento = models.ForeignKey('Equipamento', on_delete=models.CASCADE, verbose_name="Equipamento")
    data_entrega = models.DateTimeField(default=timezone.now, verbose_name="Data de Entrega")
    data_prevista_devolucao = models.DateTimeField(verbose_name="Data Prevista de Devolução")
    data_efetiva_devolucao = models.DateTimeField(null=True, blank=True, verbose_name="Data Efetiva de Devolução")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='emprestado', verbose_name="Status")
    observacao_devolucao = models.TextField(blank=True, null=True, verbose_name="Observação na Devolução")

    def __str__(self):
        return f"{self.equipamento} para {self.colaborador}"    

from django.db import models
from . import DespUser


class Estabelecimento(models.Model):
    despachante = models.OneToOneField(
        DespUser,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='Despachante',
    )
    
    telefone_comercial = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone Comercial')
    endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name='Endereço/Logradouro')
    numero = models.IntegerField(null=True, blank=True, verbose_name='Número')
    bairro = models.CharField(max_length=100, null=True, blank=True, verbose_name='Bairro')
    cep = models.CharField(max_length=8, null=True, blank=True, verbose_name='CEP')
    cidade = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, null=True, blank=True, verbose_name='Estado (UF)')

    def __str__(self):
        return f"Estabelecimento de {self.despachante.nome_completo}"

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
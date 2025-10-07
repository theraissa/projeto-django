# flake8: noqa  
from django.db import models
from django.utils import timezone
from django.conf import settings 
from desp.models.servicos import Servico


class Documento(models.Model):
    servico = models.ForeignKey(
        Servico, 
        on_delete=models.CASCADE,
        related_name='documentos', 
        verbose_name='Serviço'
    )
    
    nome = models.CharField(
        max_length=100, 
        verbose_name='Nome do Documento'
    )
    
    ordem = models.IntegerField(default=0, verbose_name='Ordem') 

    class Meta:
        verbose_name = 'Documento Necessário'
        verbose_name_plural = 'Documentos Necessários'
        ordering = ['ordem', 'nome'] 

    def __str__(self):
        return f'{self.nome} para {self.servico.nome}'
# flake8: noqa
from django.db import models
from django.utils import timezone
from django.conf import settings 


class Servico(models.Model):
    despachante = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        related_name='servicos', 
        verbose_name='Despachante'
    )
    
    nome = models.CharField(
        max_length=100, 
        verbose_name='Nome do Serviço'
    )
    
    descricao = models.TextField(
        verbose_name='Descrição Detalhada', 
        blank=True, 
        null=True
    )
    
    data_criacao = models.DateTimeField(
        default=timezone.now,
        editable=False 
    )
    
    ult_atualiz = models.DateTimeField(
        default=timezone.now 
    )

    class Meta:
        verbose_name = 'Serviço do Despachante'
        verbose_name_plural = 'Serviços do Despachante'
        ordering = ['nome']

    def save(self, *args, **kwargs):
        self.ult_atualiz = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

from django.contrib.auth.models import AbstractUser
from django.db import models


class DespUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        error_messages={'unique': ("Já existe um usuário com este e-mail.")},
        verbose_name='Email'
    )
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')  
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    telefone = models.CharField(max_length=15, verbose_name='Telefone Pessoal')

    rg = models.CharField(max_length=20, null=True, blank=True, verbose_name='RG')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    
    registro_crdd = models.CharField(max_length=255, null=True, blank=True, verbose_name='Registro CRDD')
    data_expiracao_crdd = models.DateField(null=True, blank=True, verbose_name='Data de Expiração CRDD')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo', 'cpf', 'telefone'] 
    
    def __str__(self):
        return self.nome_completo or self.email

    class Meta:
        verbose_name = 'Usuário Despachante'
        verbose_name_plural = 'Usuários Despachantes'
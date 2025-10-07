# flake8: noqa
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from desp.models.servicos import Servico


@login_required
def listar_servicos(request):
    """
    Lista todos os serviços cadastrados pelo despachante logado.
    """
    
    servicos = Servico.objects.filter(despachante=request.user)
    
    context = {
        'servicos': servicos,
        'nome_despachante': request.user.nome_completo.split()[0],  
    }
    return render(request, 'desp/services/listar_servicos.html', context)
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from desp.models.servicos import Servico


@login_required
def listar_servicos(request):

    servicos = Servico.objects.filter(despachante=request.user)
    
    context = {
        'servicos': servicos,
        'nome_despachante': request.user.nome_completo.split()[0],  
    }
    return render(request, 'desp/services/listar_servicos.html', context)


@login_required
def visualizar_servicos(request, servico_id):

    servico = get_object_or_404(Servico, pk=servico_id, despachante=request.user)
    documentos_queryset = servico.documentos.all().order_by('ordem', 'nome')

    context = {
        'servico': servico,
        'documentos_queryset': documentos_queryset, 
        'nome_despachante': request.user.nome_completo.split()[0],
    }
    return render(request, 'desp/services/visualizar.html', context)

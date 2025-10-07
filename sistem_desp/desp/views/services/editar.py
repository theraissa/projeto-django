# flake8: noqa
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from desp.models.documento import Documento
from desp.models.servicos import Servico


@login_required
def editar_servicos(request):
    """Exibe o formulário de edição ou atualiza um serviço existente."""

    service_id = request.POST.get('id_servico') 
    
    if not service_id:
        return redirect('servicos')

    servico = get_object_or_404(Servico, pk=service_id, despachante=request.user)

    if request.method == 'POST':
        nome_servico = request.POST.get('nome_servico')
        documentos = request.POST.getlist('documento_necessario[]')
        
        context = {
            'modo': 'editar',
            'servico': servico,
            'nome_servico_preenchido': nome_servico,
            'documentos_preenchidos': [doc for doc in documentos if doc]
        }
        
        if not nome_servico:
            messages.error(request, 'O nome do serviço não pode ser vazio.')
            return render(request, 'desp/services/criar_editar_servicos.html', context)

        try:
            with transaction.atomic():
                servico.nome = nome_servico
                servico.save()
                
                servico.documentos.all().delete()
                
                documentos_para_salvar = [
                    Documento(servico=servico, nome=doc_nome, ordem=i)
                    for i, doc_nome in enumerate(documentos) if doc_nome.strip()
                ]
                Documento.objects.bulk_create(documentos_para_salvar)
                
            messages.success(request, f'Serviço "{nome_servico}" atualizado com sucesso!')
            return redirect('servicos')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar o serviço: {e}')
            return render(request, 'desp/services/criar_editar_servicos.html', context)

    documentos_atuais = list(servico.documentos.all().values_list('nome', flat=True))
    
    context = {
        'modo': 'editar',
        'servico': servico,
        'documentos': documentos_atuais
    }
    return render(request, 'desp/services/criar_editar_servicos.html', context)
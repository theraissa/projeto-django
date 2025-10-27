from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from desp.models.documento import Documento
from desp.models.servicos import Servico

@login_required
def editar_servico(request):

    service_id = request.POST.get('id_servico')
    
    if not service_id:
        messages.error(request, 'ID do serviço não fornecido. Não foi possível editar.')
        return redirect('servicos')

    servico = get_object_or_404(Servico, pk=service_id, despachante=request.user)

    if request.method == 'POST':
        nome_servico = request.POST.get('nome_servico')
        descricao_servico = request.POST.get('descricao_servico', '').strip()
        documentos = request.POST.getlist('documento_necessario[]')
        documentos_atuais_do_db = list(servico.documentos.all().values_list('nome', flat=True))

        context = {
            'modo': 'editar',
            'servico': servico,
            'nome_servico_preenchido': nome_servico,
            'descricao_servico_preenchida': descricao_servico,
            'documentos_preenchidos': [doc for doc in documentos if doc],
            'documentos_atuais': documentos_atuais_do_db, 
        }
        
        if not nome_servico:
            messages.error(request, 'O nome do serviço não pode ser vazio.')
            return render(request, 'desp/services/criar_editar_servicos.html', context)

        try:
            with transaction.atomic():
                servico.nome = nome_servico
                servico.descricao = descricao_servico or None
                servico.save()
                
                servico.documentos.all().delete()
                
                documentos_para_salvar = [
                    Documento(servico=servico, nome=doc_nome, ordem=i)
                    for i, doc_nome in enumerate(documentos) if doc_nome.strip()
                ]
                Documento.objects.bulk_create(documentos_para_salvar)
                
            messages.success(request, f'Serviço "{servico.nome}" atualizado com sucesso!')
            return redirect('servicos')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar o serviço: {e}')
            return render(request, 'desp/services/criar_editar_servicos.html', context)

    documentos_atuais = list(servico.documentos.all().values_list('nome', flat=True))
    
    context = {
        'modo': 'editar',
        'servico': servico,
        'documentos_atuais': documentos_atuais 
    }
    return render(request, 'desp/services/criar_editar_servicos.html', context)
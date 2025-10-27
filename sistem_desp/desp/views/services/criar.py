from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from desp.models.documento import Documento
from desp.models.servicos import Servico

@login_required
def criar_servicos(request):
    
    if request.method == 'POST':
        nome_servico = request.POST.get('nome_servico')
        descricao_servico = request.POST.get('descricao_servico', '').strip() 
        documentos = request.POST.getlist('documento_necessario[]')
        
        context = {
            'modo': 'criar',
            'nome_servico_preenchido': nome_servico,
            'descricao_servico_preenchida': descricao_servico,
            'documentos_preenchidos': [doc for doc in documentos if doc],
            'servico': None,
            'documentos_atuais': [], 
        }
        
        if not nome_servico:
            messages.error(request, 'O nome do serviço é obrigatório.')
            return render(request, 'desp/services/criar_editar_servicos.html', context)

        try:
            with transaction.atomic():
                servico = Servico.objects.create(
                    despachante=request.user,
                    nome=nome_servico,
                    descricao=descricao_servico or None 
                )

                documentos_para_salvar = [
                    Documento(servico=servico, nome=doc_nome, ordem=i)
                    for i, doc_nome in enumerate(documentos) if doc_nome.strip()
                ]
                Documento.objects.bulk_create(documentos_para_salvar)
            
            messages.success(request, f'Serviço "{nome_servico}" criado com sucesso!')
            return redirect('servicos')
            
        except Exception as e:
            messages.error(request, f'Erro ao salvar o serviço: {e}')
            return render(request, 'desp/services/criar_editar_servicos.html', context)

    context = {
        'modo': 'criar',
        'servico': None,
        'documentos_atuais': [],
    }
    return render(request, 'desp/services/criar_editar_servicos.html', context)

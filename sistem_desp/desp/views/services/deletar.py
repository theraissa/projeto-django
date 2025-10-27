from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from desp.models.servicos import Servico


@login_required
def deletar_servico(request):
    
    if request.method == 'POST':
        service_id = request.POST.get('id_servico')
        
        if not service_id:
            messages.error(request, 'ID de serviço não fornecido.')
            return redirect('servicos')

        servico = get_object_or_404(Servico, pk=service_id, despachante=request.user)
        
        try:
            nome_servico = servico.nome
            servico.delete()             
            messages.success(request, f'Serviço "{nome_servico}" excluído com sucesso.')
            
        except Exception as e:
            messages.error(request, f'Erro ao excluir o serviço: {e}')
        
    return redirect('servicos')

@login_required
def deletar_servico(request):
    """Deleta um serviço existente."""
    
    if request.method == 'POST':
        service_id = request.POST.get('id_servico')
        
        if not service_id:
            messages.error(request, 'ID de serviço não fornecido.')
            return redirect('servicos')

        # Busca o serviço, garantindo que ele pertença ao usuário logado e existe
        # Se não encontrar ou não pertencer ao usuário, lança 404
        servico = get_object_or_404(Servico, pk=service_id, despachante=request.user)
        
        try:
            nome_servico = servico.nome
            servico.delete() 
            # O CASCADE (no Model) garante que os DocumentoServico relacionados também sejam excluídos.
            
            messages.success(request, f'Serviço "{nome_servico}" excluído com sucesso.')
            
        except Exception as e:
            messages.error(request, f'Erro ao excluir o serviço: {e}')
        
    return redirect('servicos')
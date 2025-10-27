from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from desp.models import DespUser 
from desp.models.estabelecimento import Estabelecimento
from datetime import date


def get_optional_field(request, field_name, current_value):
    """Obtém o valor do POST, retornando o valor existente se o POST for vazio/None."""
    post_value = request.POST.get(field_name, '').strip()
    return post_value if post_value else current_value


@login_required
def perfil_desp(request):
    despachante = request.user 
    estabelecimento, created = Estabelecimento.objects.get_or_create(despachante=despachante)

    if request.method == 'POST':
        try:
            with transaction.atomic():
                
                despachante.nome_completo = get_optional_field(request, 'nome_desp', despachante.nome_completo)
                despachante.rg = get_optional_field(request, 'rg_desp', despachante.rg)
                despachante.telefone = get_optional_field(request, 'tele_pessoal_desp', despachante.telefone)
                despachante.registro_crdd = get_optional_field(request, 'regis_crdd', despachante.registro_crdd)
                
                data_nascimento_post = request.POST.get('nasc_desp', '').strip()
                if data_nascimento_post:
                    despachante.data_nascimento = data_nascimento_post
                
                data_expiracao_post = request.POST.get('data_exp_regis', '').strip()
                if data_expiracao_post:
                    despachante.data_expiracao_crdd = data_expiracao_post

                nova_senha = request.POST.get('senha_desp', '').strip()
                confirmar_senha = request.POST.get('confirmar_senha', '').strip()
                
                if nova_senha:
                    if nova_senha == confirmar_senha:
                        despachante.set_password(nova_senha) 
                        messages.info(request, "Sua senha foi atualizada com sucesso.")
                    else:
                        messages.error(request, "A nova senha e a confirmação não coincidem. A senha não foi alterada.")
                        return redirect('perfil') 

                despachante.save()

                estabelecimento.telefone_comercial = get_optional_field(request, 'tele_comercial', estabelecimento.telefone_comercial)
                estabelecimento.endereco = get_optional_field(request, 'endereco_desp', estabelecimento.endereco)
                estabelecimento.numero = get_optional_field(request, 'num_desp', estabelecimento.numero)
                estabelecimento.bairro = get_optional_field(request, 'bairro_desp', estabelecimento.bairro)
                estabelecimento.cep = get_optional_field(request, 'cep_desp', estabelecimento.cep)
                estabelecimento.cidade = get_optional_field(request, 'cidade_desp', estabelecimento.cidade)
                estabelecimento.estado = get_optional_field(request, 'estado_desp', estabelecimento.estado)
                
                estabelecimento.save()

                justificativa = request.POST.get('justificativa', '').strip()
                if justificativa:
                    messages.info(request, "Sua solicitação de alteração de dados foi enviada ao administrador.")
                
                messages.success(request, "Seus dados de perfil foram atualizados com sucesso.")
                
        except Exception as e:
            messages.error(request, f"Ocorreu um erro inesperado ao salvar: {e}")

        return redirect('perfil') 

    context = {
        'nome_despachante': despachante.nome_completo.split()[0], 
        'despachante': despachante, 
        'estabelecimento': estabelecimento,
    }
    return render(request, 'desp/func/perfil.html', context)

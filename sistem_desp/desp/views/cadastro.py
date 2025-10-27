from django.shortcuts import render, redirect
from django.contrib import messages
from desp.models.desp_user import DespUser
from django.db import IntegrityError


def cadastro_desp(request):
    
    context = {} 
    
    if request.method == 'POST':
        
        nome_completo = request.POST.get('nome_completo')
        cpf_raw = request.POST.get('cpf')
        telefone_raw = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confir = request.POST.get('senha_confir')

        cpf_limpo = cpf_raw.replace('.', '').replace('-', '') 
        telefone_limpo = telefone_raw.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

        context.update({
            'nome_completo': nome_completo,
            'cpf': cpf_raw, 
            'telefone': telefone_raw,
            'email': email,
        })
        
        erros_validacao = {} 
        
        if senha != senha_confir:
            erros_validacao['senha_confir'] = 'As senhas não coincidem.'
        if len(senha) < 8:
            erros_validacao['senha'] = 'A senha deve ter no mínimo 8 caracteres.'
        
        if len(cpf_limpo) != 11:
            erros_validacao['cpf'] = 'O CPF deve ter 11 dígitos (após a limpeza).'

        if erros_validacao:
            for campo, mensagem in erros_validacao.items():
                messages.error(request, f'{campo.upper()}: {mensagem}') 
            return render(request, 'cadastro.html', context)

        try:
            DespUser.objects.create_user(
                username=email, 
                email=email,
                password=senha,
                nome_completo=nome_completo,
                cpf=cpf_limpo, 
                telefone=telefone_limpo 
            )
            messages.success(request, 'Cadastro realizado com sucesso! Agora faça login.')
            return redirect('login') 

        except IntegrityError:
            messages.error(request, 'Erro: Este email ou CPF já está cadastrado.')
            return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html', context)
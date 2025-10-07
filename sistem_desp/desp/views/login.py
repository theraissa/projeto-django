# flake8: noqa
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 


def user_login(request): 

    if request.method == 'POST':
        email = request.POST.get('email-login')
        senha = request.POST.get('senha-login')

        context = {'email': email} 

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            auth_login(request, user) 
            messages.success(request, f"Bem-vindo(a), {user.nome_completo.split()[0]}!")
            return redirect('servicos') 
        else:
            messages.error(request, 'Email ou senha inválidos. Tente novamente.')
            return render(request, 'login.html', context)
        
    return render(request, 'login.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 
from django.urls import reverse
from desp.models import DespUser 

EMAIL_SESSION_KEY = 'login_email_rapido_desp'


def login_rapido(request):

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()

        if not email:
            messages.error(request, "Por favor, informe seu e-mail.")
            return redirect(request.META.get('HTTP_REFERER', reverse('home'))) 

        try:
            DespUser.objects.get(email=email) 
        except DespUser.DoesNotExist:
            messages.error(request, "E-mail não cadastrado. Verifique ou cadastre-se.")
            return redirect(request.META.get('HTTP_REFERER', reverse('home'))) 
        
        request.session[EMAIL_SESSION_KEY] = email
        return redirect('login') 
    return redirect(reverse('home'))


def user_login(request): 

    context = {}
    
    if request.method == 'GET':
        email_from_session = request.session.get(EMAIL_SESSION_KEY)
        if email_from_session:
            context['email_preenchido'] = email_from_session
    
    if request.method == 'POST':
        email = request.POST.get('email-login')
        senha = request.POST.get('senha-login')
        
        context['email_preenchido'] = email 

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            auth_login(request, user) 
            
            if EMAIL_SESSION_KEY in request.session:
                del request.session[EMAIL_SESSION_KEY]
                
            messages.success(request, f"Bem-vindo(a), {user.nome_completo.split()[0]}!")
            return redirect('servicos') 
        else:
            messages.error(request, 'Senha inválida. Tente novamente.') 
            return render(request, 'login.html', context)
        
    return render(request, 'login.html', context)

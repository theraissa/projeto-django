from django.shortcuts import render


def chamado_desp(request):
    context = {
        'nome_despachante': request.user.nome_completo.split()[0]
    }
    return render(request, 'desp/func/chamado.html', context)
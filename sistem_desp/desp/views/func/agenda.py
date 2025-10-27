from django.shortcuts import render


def agenda_desp(request):
    context = {
        'nome_despachante': request.user.nome_completo.split()[0]
    }
    return render(request, 'desp/func/agenda.html', context)
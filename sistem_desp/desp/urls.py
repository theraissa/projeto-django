from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro-desp/', views.cadastro_desp, name='cadastro_desp'),
    path('login/', views.user_login, name='login'),
    path('login-rapido/', views.login_rapido, name='login_rapido'),

    path('despachante/servicos/', views.listar_servicos, name='servicos'),
    path('despachante/servicos/<int:servico_id>/', views.visualizar_servicos, name='visualizar_servico'), 
    path('despachante/criar-servicos/', views.criar_servicos, name='criar_servicos'),
    path('despachante/editar-servico/', views.editar_servico, name='editar_servico'),
    path('despachante/deletar-servico/', views.deletar_servico, name='deletar_servico'),
    path('despachante/chamados/', views.chamado_desp, name='chamados'),
    path('despachante/agendamentos/', views.agenda_desp, name='agendamentos'),
    path('despachante/perfil/', views.perfil_desp, name='perfil'),
]

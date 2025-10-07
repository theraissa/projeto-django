from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro-desp/', views.cadastro_desp, name='cadastro_desp'),
    path('login/', views.user_login, name='login'),

    path('despachante/servicos/', views.listar_servicos, name='servicos'),
    path('despachante/criar-servicos/', views.criar_servicos, name='criar_servicos'),
    path('despachante/editar-servicos/', views.editar_servicos, name='editar_servicos'),

    # path('despachante/deletar-servico/', views.deletar_servico, name='deletar_servico'),
    # path('despachante/chamados/', views.chamados_despachante, name='chamados'),
    # path('despachante/agendamentos/', views.agendamentos_despachante, name='agendamentos'),
    # path('despachante/perfil/', views.perfil_despachante, name='perfil'),
]

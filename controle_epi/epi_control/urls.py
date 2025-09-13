from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colaboradores/cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('colaboradores/', views.listar_colaboradores, name='listar_colaboradores'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/excluir/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
    path('equipamentos/cadastrar/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('controle_epi/cadastrar/', views.cadastrar_controle_epi, name='cadastrar_controle_epi'),
    path('relatorios/', views.relatorio_colaboradores, name='relatorio_colaboradores'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/excluir/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
]
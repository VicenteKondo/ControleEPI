
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaborador
from .forms import ColaboradorForm 
from .forms import EmprestimoForm
from .models import ControleEPI
from .models import Emprestimo

def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save() # O .save() do ModelForm cria o objeto no banco de dados
            messages.success(request, 'Colaborador cadastrado com sucesso!') #
            return redirect('cadastrar_colaborador') # Redireciona para a mesma página para limpar o formulário
        else:
            # Se o formulário não for válido, as mensagens de erro serão enviadas com o próprio form
            messages.error(request, 'Falha no cadastro. Verifique os dados informados.') 
    else:
        # Se a requisição for GET, apenas cria um formulário em branco
        form = ColaboradorForm()

    return render(request, 'epi_control/cadastrar_colaborador.html', {'form': form})

def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all() # Busca todos os colaboradores no banco
    return render(request, 'epi_control/listar_colaboradores.html', {'colaboradores': colaboradores})

def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id) # Pega o colaborador específico ou retorna erro 404

    if request.method == 'POST':
        # Preenche o formulário com os dados enviados e os dados existentes do colaborador
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('listar_colaboradores')
    else:
        # Ao abrir a página, preenche o formulário com os dados atuais do colaborador
        form = ColaboradorForm(instance=colaborador)

    return render(request, 'epi_control/editar_colaborador.html', {'form': form, 'colaborador': colaborador})

def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    messages.success(request, 'Colaborador excluído com sucesso!')
    return redirect('listar_colaboradores')

def home(request):
    return render(request, 'epi_control/home.html')

from .models import Equipamento
from .forms import EquipamentoForm

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
        else:
            messages.error(request, 'Falha ao cadastrar o equipamento. Verifique os dados informados.')
    else:
        form = EquipamentoForm()

    return render(request, 'epi_control/cadastrar_equipamento.html', {'form': form})

def cadastrar_controle_epi(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Controle de EPI cadastrado com sucesso!')
        else:
            messages.error(request, 'Falha ao cadastrar o controle de EPI. Verifique os dados informados.')
    else:
        form = EmprestimoForm()

    return render(request, 'epi_control/cadastrar_controle_epi.html', {'form': form})

def editar_controle_epi(request, id):
    controle = get_object_or_404(ControleEPI, id=id)
    if request.method == 'POST':
        form = ControleEPIForm(request.POST, instance=controle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Controle de EPI atualizado com sucesso!')
            return redirect('cadastrar_controle_epi')
    else:
        form = ControleEPIForm(instance=controle)

    return render(request, 'epi_control/editar_controle_epi.html', {'form': form, 'controle': controle})

def excluir_controle_epi(request, id):
    controle = get_object_or_404(ControleEPI, id=id)
    if request.method == 'POST':
        controle.delete()
        messages.success(request, 'Controle de EPI excluído com sucesso!')
        return redirect('cadastrar_controle_epi')

    return render(request, 'epi_control/excluir_controle_epi.html', {'controle': controle})

def relatorio_colaboradores(request):
    nome = request.GET.get('nome', '')  # Obtém o nome do colaborador da query string
    if nome:  # Se o nome foi fornecido na pesquisa
        emprestimos = Emprestimo.objects.filter(
            colaborador__nome_completo__icontains=nome
        )
    else:  # Caso contrário, retorna todos os registros
        emprestimos = Emprestimo.objects.all()

    return render(request, 'epi_control/relatorio_colaboradores.html', {'emprestimos': emprestimos})

def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('home')
    else:
        form = ColaboradorForm(instance=colaborador)

    return render(request, 'epi_control/editar_colaborador.html', {'form': form})

def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('home')

    return render(request, 'epi_control/excluir_colaborador.html', {'colaborador': colaborador})

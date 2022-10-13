from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Paper, Prova, DadosCadastro
from .forms import *

# Create your views here.


def movel(request, link_prova):
    prova = get_object_or_404(Prova, link=link_prova)
    if request.method == 'GET':
        form = Cadastro()
    else:
        form = Cadastro(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = Cadastro()
    return render(request, 'elefante/telacriacao.html', {'form': form, 'prova': prova})


def resolver(request, link_prova):
    prova = get_object_or_404(Prova, link=link_prova)
    paper = get_list_or_404(Paper, id_prova=prova.id)
    if request.method == 'GET':
        form = Cadastro()
    else:
        form = Cadastro(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = Cadastro()
    return render(request, 'elefante/telaresolucao.html', {'form': form, 'papers': paper})

def sign(request):
    if request.method == 'GET':
        form = Registro()
        return render(request, 'elefante/telalogin.html', {'form': form})
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conta = DadosCadastro.objects.filter(email=email, senha=senha)
        if conta:
            # form = Cadastro()
            return render(request, 'elefante/telaresolucao.html')
        else:            
            form = Registro()
            return redirect('login')

def cadastrin(request):
    if request.method == 'GET':
        form = cadaa()
        return render(request, 'elefante/telacadastro.html', {'form': form})
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cont = DadosCadastro.objects.filter(email=email, senha=senha)
        if cont:
            form = cadaa()
            return redirect('cadastro')
        else:
            form = cadaa(request.POST)
            if form.is_valid():
                form = form.save()
                form = Registro()
                return redirect('login')
            else:
                form = cadaa()
                return redirect('cadastro')
#
# def redefinir(request, id):
#     aa = get_object_or_404(DadosCadastro, id=id_usuario)
#     form = Redefinir(request.POST)
#
#     if request.method == 'POST':
#
#
#


def homepage(request):
    return render(request, 'elefante/telahomepage.html')


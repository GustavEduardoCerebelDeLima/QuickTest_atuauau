from django.shortcuts import render, redirect
from .forms import Cadastro, Registro, cadaa
from .models import dados_cadastro
# Create your views here.


def movel(request):
    # if request.method == 'GET':
        return render(request, 'elefante/telacriacao.html')
    # else:
    #     form = Cadastro(request.POST)
    #     if form.is_valid():
    #         cadastro = form.save()
    #         form = Cadastro()
    #         return render(request, 'elefante/telacriacao.html', {'form': form})

        # else:
        #     form = Cadastro()
        #     return render(request, 'elefante/telacriacao.html', {'form': form})

def sign(request):
    if request.method == 'GET':
        form = Registro()
        return render(request, 'elefante/telalogin.html', {'form': form})
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conta = dados_cadastro.objects.filter(email=email, senha=senha)
        if conta:
            form = Cadastro()
            return redirect('criacao')
        else:            
            form = Registro()
            return redirect('login')
def cadastrin(request):
    if request.method == 'GET':
        form = cadaa()
        return render(request, 'elefante/telacadastro.html', {'form': form})
    # else:
    #     email = request.POST.get('email')
    #     senha = request.POST.get('senha')
    #     cont = dados_cadastro.objects.filter(email=email, senha=senha)
    #     if cont:
    #         form = cadaa()
    #         return redirect('cadastro')
        # else:
        #     if form.is_valid():
        #         form = form.save()
        #         form = Registro()
        #         return redirect('login')
        #     else:
        #         form = cadaa()
        #         return redirect('cadastro')


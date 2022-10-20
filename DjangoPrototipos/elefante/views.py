from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def SignUp(request):
    if request.method == 'GET':
        form = cadaa()
        return render(request, 'elefante/register.html', {'form': form})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password1')

        user = User.objects.filter(email=email).first()

        if user:
            form = cadaa()
            return redirect(request, 'elefante/register.html', {'form': form})
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('accounts/login')
@login_required
def movel(request, link_prova):
    prova = get_object_or_404(Prova, link=link_prova)
    paper = Paper.objects.filter(id_prova=prova.id, tipo_user='C')
    if request.method == 'GET':
        form = Cadastro()
    else:
        form = Cadastro(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = Cadastro()
    return render(request, 'elefante/telacriacao.html', {'form': form, 'prova': prova, 'papers': paper})

@login_required
def resolver(request, link_prova):
    prova = get_object_or_404(Prova, link=link_prova)
    paper = get_list_or_404(Paper, id_prova=prova.id, tipo_user='C')
    if request.method == 'GET':
        form = Cadastro()
    else:
        form = Cadastro(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = Cadastro()
    return render(request, 'elefante/telaresolucao.html', {'form': form, 'papers': paper, 'id': prova.id, 'link': link_prova})

@login_required
def nota(request, link_prova, usuario):
    prova = get_object_or_404(Prova, link=link_prova)
    paper = get_list_or_404(Paper, id_prova=prova.id, usuario=usuario)
    return render(request, 'elefante/nota.html', {'notas': paper})

# def sign(request):
#     if request.POST == 'POST':
#         form = UserCreationForm()
#         if form.is_valid():
#             form.save()
#     messages.success(request, 'Account created successfully')
#
#     else:
#     form = UserCreationForm()
#
#
# context = {
#     'form': form
# }
# return render(request, 'register.html', context)


# if request.method == 'GET':
    #     form = Registro()
    #     return render(request, 'elefante/login.html', {'form': form})
    # else:
    #     email = request.POST.get('email')
    #     senha = request.POST.get('senha')
    #     conta = DadosCadastro.objects.filter(email=email, senha=senha)
    #     if conta:
    #         # form = Cadastro()
    #         return render('resolv')
    #     else:
    #         form = Registro()
    #         return redirect('login')




    # if request.method == 'GET':
    #     form = cadaa()
    #     return render(request, 'elefante/register.html', {'form': form})
    # else:
    #     email = request.POST.get('email')
    #     senha = request.POST.get('senha')
    #     cont = DadosCadastro.objects.filter(email=email, senha=senha)
    #     if cont:
    #         form = cadaa()
    #         return redirect('cadastro')
    #     else:
    #         form = cadaa(request.POST)
    #         if form.is_valid():
    #             form = form.save()
    #             form = Registro()
    #             return redirect('login')
    #         else:
    #             form = cadaa()
    #             return redirect('cadastro')
#
# def redefinir(request, id):
#     aa = get_object_or_404(DadosCadastro, id=id_usuario)
#     form = Redefinir(request.POST)
#
#     if request.method == 'POST':


@login_required
def homepage(request):
    return render(request, 'elefante/telahomepage.html')


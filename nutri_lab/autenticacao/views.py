from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from .utils import password_is_valid

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        print(senha, confirmar_senha)
       
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username,
                email=email,
                password=senha,
                is_active=False)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado no sistema')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR, 'ERRO interno no sistema')
            return redirect('/auth/cadastro')        
        

def logar(request):    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')        
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/')

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')

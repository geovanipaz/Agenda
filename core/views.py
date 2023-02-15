from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from core.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"usuario ou senha inválidos")
    
    return redirect('/')



@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    #eventos  = Evento.objects.all()
    eventos = Evento.objects.filter(usuario=usuario)
    resposta = {'eventos':eventos}
    return render(request,'agenda.html', resposta)

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def evento_submit(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_criacao = request.POST.get('data_criacao')
        descricao = request.POST.get('descricao')
        usuario = request.user
    
        Evento.objects.create(titulo=titulo,
                            data_criacao=data_criacao,
                            desricao=descricao,
                            usuario=usuario)
        
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request,id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')


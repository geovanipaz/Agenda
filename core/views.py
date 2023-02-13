from django.shortcuts import render, HttpResponse

from core.models import Evento
# Create your views here.

def lista_eventos(request):
    #usuario = request.user
    eventos  = Evento.objects.all()
    resposta = {'eventos':eventos}
    return render(request,'agenda.html', resposta)

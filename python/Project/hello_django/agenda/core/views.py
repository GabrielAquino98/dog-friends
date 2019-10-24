from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from core.models import Evento
from django.contrib.auth import authenticate, login

# Create your views here.

def retorna_local(request, titulo_evento):
    #Evento.objects.get(titulo=titulo_evento) == select * from table where titulo = 'titulo_evento'
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h2>Local do Evento: {}</h2>'.format(evento.local_evento))

def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def lista_eventos(request):
    #evento = Evento.objects.filter(usuario = usuario)
    evento = Evento.objects.all
    dados = {'eventos' : evento}
    return render(request, 'agenda.html', dados)

#def index(request):
#    return redirect('/agenda/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
    else:
        return redirect('/')
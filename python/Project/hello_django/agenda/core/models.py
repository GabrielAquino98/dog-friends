from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao =  models.DateTimeField(auto_now=True)
    local_evento = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #Estou informando qual vai ser o nome da tabela
    class Meta:
       db_table = 'evento'

    def __str__(self):
        return self.titulo

    def retornaEvento(titulo_evento):
        evento = Evento.object.get(titulo=titulo_evento)
        return evento

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')

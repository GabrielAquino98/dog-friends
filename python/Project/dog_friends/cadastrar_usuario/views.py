from django.shortcuts import render, HttpResponse
from rest_framework import  generics
from .serializers import ProprietarioSerializer, EnderecoSerializer, EnderecoPropSerializer
from cadastrar_usuario.models import TbProprietario, TbEndereco,  TbEnderecoProp
# Create your views here.

#CRIAR ALGORITMO PARA CADASTRO DE USUARIO

def Valida_CPF_Proprietario(cpf_proprietario):
    prop = TbProprietario.objects.get(cpf=cpf_proprietario)

    if(prop is None):
        return True
    else:
        return False

def Valida_Email_Proprietario(email_proprietario):
    prop = TbProprietario.objects.get(email =email_proprietario)

    if(prop is None):
        return True
    else:
        return False


def Cadastra_Proprietario(request):
    #Valida se não existe um ussuario na base com o cpf e email informado
    #Caso não exista a função Valida Proprietario retorna verdadeiro
    if(Valida_CPF_Proprietario(request.POST.get('cpf'))) :
        if (Valida_Email_Proprietario(request.POST.get('email'))):
            cpf = request.POST.get('cpf')
            nome = request.POST.get('nome')
            telefone = request.POST.get('telefone')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            logradouro = request.POST.get('logradouro')
            cep = request.POST.get('CEP')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            foto = request.POST.get('foto')
            descricao = request.POST.get('descricao')
            sexo = request.POST.get('sexo')
            data_nascimento = request.POST.get('dt_nascimento')

            if(TbProprietario.objects.add(cpf, nome,telefone,email,senha,
                                         foto,descricao,sexo,data_nascimento)):
                endereco = TbEndereco.objects.add(cep, logradouro, numero, bairro,cidade,estado)

                TbEnderecoProp.objects.add(endereco.id, cpf)
                return HttpResponse( 'Uhuul, seu usuario foi cadastrado com sucesso :)')
            else:
                return HttpResponse('Infelizmente não foi possivel cadastrar seu usuario :(')
        else:
            return HttpResponse('Opa! Aparentemente já existe um usuario cadastrado com esse email!')
    else:
        return HttpResponse('Opa! Aparentemente já existe um usuario cadastrado com esse CPF!')




class ProprietarioList(generics.ListCreateAPIView):

    queryset = TbProprietario.objects.all()
    serializer_class = ProprietarioSerializer

class EnderecoList(generics.ListCreateAPIView):

    queryset = TbEndereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoPropList(generics.ListCreateAPIView):

    queryset = TbEnderecoProp.objects.all()
    serializer_class = EnderecoPropSerializer
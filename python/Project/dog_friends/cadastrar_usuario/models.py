# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbDogwalker(models.Model):
    cpf = models.CharField(db_column='CPF', primary_key=True, max_length=11)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=100)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=30)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=20)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dt_nascimento = models.DateField(db_column='DT_NASCIMENTO', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='FOTO', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)  # Field name made lowercase.
    status_dw = models.CharField(db_column='STATUS_DW', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tamanho_camisa = models.CharField(db_column='TAMANHO_CAMISA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    md_avaliacao = models.FloatField(db_column='MD_AVALIACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_dogwalker'


class TbEndereco(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='LOGRADOURO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='COMPLEMENTO', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_endereco'


class TbEnderecoDw(models.Model):
    id_end = models.ForeignKey(TbEndereco, models.DO_NOTHING, db_column='ID_END', blank=True, null=True)  # Field name made lowercase.
    cpf_dw = models.ForeignKey(TbDogwalker, models.DO_NOTHING, db_column='CPF_DW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_endereco_dw'


class TbProprietario(models.Model):
    cpf = models.CharField(db_column='CPF', primary_key=True, max_length=11)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=100)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=30)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=20)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dt_nascimento = models.DateField(db_column='DT_NASCIMENTO', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='FOTO', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_proprietario'


class TbEnderecoProp(models.Model):
    id_end = models.ForeignKey(TbEndereco, models.DO_NOTHING, db_column='ID_END', blank=True, null=True)  # Field name made lowercase.
    cpf_prop = models.ForeignKey(TbProprietario, models.DO_NOTHING, db_column='CPF_PROP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_endereco_prop'

class TbAnimal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=10)  # Field name made lowercase.
    dt_nascimento = models.DateField(db_column='DT_NASCIMENTO', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='FOTO', blank=True, null=True)  # Field name made lowercase.
    tipo_animal = models.CharField(db_column='TIPO_ANIMAL', max_length=10)  # Field name made lowercase.
    raca = models.CharField(db_column='RACA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    porte = models.CharField(db_column='PORTE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    faz_atividade = models.CharField(db_column='FAZ_ATIVIDADE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comportamento = models.TextField(db_column='COMPORTAMENTO', blank=True, null=True)  # Field name made lowercase.
    cpf_prop = models.ForeignKey(TbProprietario, models.DO_NOTHING, db_column='CPF_PROP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_animal'

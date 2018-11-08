from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits = 5,decimal_places = 2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clientes_fotos',null = True, blank= True)



class Tipo_Premio(models.Model):
    _DATABASE = 'mssql'

    class Meta:
        db_table = "[DW].[PREMIO_TIPO_ID]"
    descricao = models.CharField(max_length=200)


    def __str__(self):
     return self.descricao

class Departamentos(models.Model):
    _DATABASE = 'mssql_'

    class Meta:
        db_table = "[DBO].[AUX_Grupo_Segmento]"

    CC_Custo = models.CharField(max_length=11,primary_key=True)
    Ativo = models.CharField(max_length=3)
    Descricao =  models.CharField(max_length=100)
    Grupo = models.CharField(max_length=50)

class Funcionarios(models.Model):
    _DATABASE = 'func_funcionarios'

    class Meta:
        db_table = "[DBO].[V_ML_FUNCIONARIO]"

    CPF = models.CharField(max_length=11, primary_key=True)
    NOME = models.CharField(max_length=100)


class Premio(models.Model):
    _DATABASE = 'premiacao'

    class Meta:
        db_table = "[DBO].[GESTAO_PREMIACAO]"

    chave_premio  = models.CharField(max_length=11, primary_key=True)
    dt_inclus = models.DateTimeField()
    ctr_custo = models.CharField(max_length=12)
    tipo = models.PositiveIntegerField()
    competenc = models.CharField(max_length=7)
    observacao = models.CharField(max_length=1000,blank=True,null=True)
    cpf =  models.PositiveIntegerField()
    nota_camp = models.CharField(max_length=20,blank=True,null=True)
    vlr_base = models.DecimalField(max_digits=7,decimal_places=2)
    falta_just = models.CharField(max_length=3,blank=True, null=True)
    falta_inju = models.CharField(max_length=3,blank=True, null=True)
    vlr_pagar = models.DecimalField(max_digits=7,decimal_places=2)
    estagio = models.PositiveIntegerField()
    solicitante = models.TextField()
    dt_env_cpa = models.DateTimeField()
    dt_pagamento = models.DateTimeField()
    sit_empre = models.CharField(max_length=50,blank=True, null=True)


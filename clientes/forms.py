from django.forms import ModelForm
from .models import Person,Tipo_Premio,Departamentos,Funcionarios,Premio

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name', 'age','salary','bio','photo']

class TipoPremioForm(ModelForm):
    class Meta:
        model = Tipo_Premio
        fields = ['descricao']

class DepartamentosForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = ['Descricao','Ativo','CC_Custo','Grupo']

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['CPF','NOME']

class PremioForm(ModelForm):
    class Meta:
        model = Premio
        fields = ['chave_premio','dt_inclus','ctr_custo','tipo','competenc','observacao',
                  'cpf','nota_camp','vlr_base','faltas_just','faltas_inju','vlr_pagar',
                  'estagio','solicitante','dt_pagamento','dt_env_cpa']
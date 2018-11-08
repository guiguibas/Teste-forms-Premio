###tratando o arquivo de premiação

# importando bibliotecas
import tkinter as tki
import pandas as pd
import pyodbc as odbc
from fnmatch import fnmatch  # criador MASCARA
import datetime as dt
import numpy as np
from pycpfcnpj import cpfcnpj
import string
import pycpfcnpj
from .views import tipopremio

def valida_arq(request):
    gui = 1
    return gui

# importando arquivo execel
nomearq = input('Digite o Nome do arquivo para importação: ')
caminho = 'N:\Planejamento\PLAN\PREMIACOES\FORMULARIOS DE PREMIACAO\\'
arquivo = pd.read_excel(caminho + nomearq + '.xlsm')
validacao = []

competencia = arquivo['Unnamed: 9'][:5][0]
ccusto = arquivo['Unnamed: 9'][:5][3]
nota = arquivo['Unnamed: 9'][:5][4]


if arquivo['Unnamed: 9'][:5][1] == 'Bonificação (NF)':
    tipo = 1
elif arquivo['Unnamed: 9'][:5][1] == 'Premiação - Ranking':
    tipo = 2
elif arquivo['Unnamed: 9'][:5][1] == 'Premiação - Receita':
    tipo = 3
elif arquivo['Unnamed: 9'][:5][1] == 'Campanha Motivacional':
    tipo = 4
else:
    validacao.append('Faltou o tipo de Premio')

arquivo = arquivo[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8']]
arquivo = arquivo[7:]
arquivo = arquivo.dropna(axis=0, how='all')

arquivo['competenc'] = competencia
arquivo['ctr_custo'] = ccusto
arquivo['nota_camp'] = nota
arquivo['tipo'] = tipo



# Excluindo colunas'carteira' desnecessarias
# arquivo = arquivo.drop(['Unnamed: 0', 'Unnamed: 1'] ,axis = 1)


arquivo.rename(columns={'Unnamed: 2': 'cpf', 'Unnamed: 3': 'nome',
                        'Unnamed: 4': 'vlr_base', 'Unnamed: 5': 'faltas_just',
                        'Unnamed: 6': 'faltas_inju', 'Unnamed: 7': 'vlr_pagar', 'Unnamed: 8': 'observacao'
                        }, inplace=True)

arquivo['ctr_custo'] = arquivo['ctr_custo'].str.strip()
arquivo['cpf'] = arquivo['cpf'].apply(str)
arquivo['cpf'] = arquivo['cpf'].str.strip()

#limpando CPF
purge_full = str.maketrans(dict.fromkeys("/*-+.,!@#$%¨&)'(_}{`^?:><;~][´=-¹²³£¢¬§ªº°"))
purge_letras = str.maketrans(dict.fromkeys('QWERTYUIOPASDFGHJKLÇZXCVBNM'))

arquivo['cpf'] = arquivo.cpf.str.upper()
arquivo['cpf'] = arquivo.cpf.str.translate(purge_full)
arquivo['cpf'] = arquivo.cpf.str.translate(purge_letras)
arquivo['cpf'] = arquivo.cpf.str.replace(' ', '')
arquivo['cpf'] = arquivo.cpf.str.lstrip('0')
arquivo['cpf'] = arquivo['cpf'].apply(np.int)
#preenchenco com zeros a esquerda
arquivo['cpf'] = arquivo['cpf'].apply(np.str)
arquivo['cpf'] = arquivo.cpf.str.zfill(11)


# valida campos em branco

qtde_linhas_total_do_arquivo = arquivo.shape[0]
if arquivo['cpf'].count() != qtde_linhas_total_do_arquivo:
    validacao.append('Existes CPF em branco, Devolver arquivo')

if arquivo['vlr_base'].count() != qtde_linhas_total_do_arquivo:
    validacao.append('Existe algum caso de Valor Base em branco, Devolver arquivo')

if arquivo['vlr_pagar'].count() != qtde_linhas_total_do_arquivo:
    validacao.append('Existe algum caso de Valor Pagar em branco, Devolver arquivo')

if arquivo['faltas_just'].count() == 0 and arquivo['faltas_just'].count() == 0:
    arquivo['faltas_just'] = np.NaN
    arquivo['faltas_inju'] = np.NaN



arquivo['chave_premio'] = arquivo['tipo'].astype(int).apply(str) + '|' \
                          + arquivo['competenc'].apply(str) + '|' \
                          + arquivo['ctr_custo'].apply(str) + '|' \
                          + arquivo['cpf'].apply(str)

# criando campos defalt premiação
dtatual = dt.datetime.now()
arquivo['dt_inclus'] = dtatual.strftime('%Y-%m-%d %H:%M:%S.000')
arquivo['solicitante'] = input('Digite o nome do Solicitante: ')
arquivo['dt_pagamento'] = pd.NaT
arquivo['dt_envio_cpa'] = pd.NaT
arquivo['estagio'] = 7

# inicianco conexão com SQL
cn = odbc.connect('DRIVER={SQL Server};SERVER=plan01spo15;DATABASE=PRODUCAO;UID=planejamento;PWD=pl@n1234')
# cn1 = odbc.connect('DRIVER={SQL Server};SERVER=plan01spo15;DATABASE=HOMOLOGACAO;UID=planejamento;PWD=pl@n1234')

# excutor de scripts SQL
cursor = cn.cursor()

# tirando cabeçalho


# alterando o estagio para demitido
sqldemitido = f"""  SELECT BASE.CPF, BASE.SIT_EMPRE, BASE.DT_ADMISSAO FROM (
                    SELECT CPF, SIT_EMPRE,DT_ADMISSAO FROM  DW..V_ML_FUNCIONARIO) as base
                    INNER JOIN ( SELECT CPF,MAX(DT_ADMISSAO) AS DT_ADMISSAO FROM DW..V_ML_FUNCIONARIO 
                    GROUP BY CPF) AS C
                    ON BASE.CPF = C.CPF AND BASE.DT_ADMISSAO = C.DT_ADMISSAO"""

cpf_sit = pd.read_sql(sqldemitido, cn)
arquivo = pd.merge(arquivo
                   , cpf_sit
                   , left_on='cpf'
                   , right_on='CPF'
                   , how='left'
                   )

# arquivo['sit_empre'] = np.where(arquivo.SIT_EMPRE == 'DEMITIDO', 9, 7)
arquivo['sit_empre'] = arquivo.SIT_EMPRE

if arquivo['CPF'].count() != arquivo['cpf'].count():
    validacao.append('Existem CPFs invalidos, Retorne ao Solicitante')

# criando listas para cruzar nomes de colunas
qtde_linhas = len(arquivo)
obj_lista_de_colunas = []
sql_lista_de_colunas = []

# validando Centro de Custo
sql = f" SELECT CC_Custo from Controladoria..AUX_Grupo_Segmento "
ccusto = pd.read_sql(sql, cn)

arquivo = pd.merge(arquivo
                   , ccusto
                   , left_on='ctr_custo'
                   , right_on='CC_Custo'
                   , how='left'
                   )
if arquivo['CC_Custo'].count() == 0:
    validacao.append('Centro de Custo inexistente')

if arquivo['vlr_pagar'].count() == np.NaN:
    arquivo['vlr_pagar'] = arquivo['vlr_base']

# dropando colunas desnecessarias
arquivo = arquivo.drop('CPF', axis=1)
arquivo = arquivo.drop('SIT_EMPRE', axis=1)
arquivo = arquivo.drop('nome', axis=1)
arquivo = arquivo.drop('CC_Custo', axis=1)
arquivo = arquivo.drop('DT_ADMISSAO', axis=1)


# atribuindo nome colunas do arquivo a variavel
for x in arquivo:
    obj_lista_de_colunas.append(x)

# capturando os nomes da coluna da tabela sql
lista_de_colunas = cursor.columns(table='GESTAO_PREMIACAO', schema='DBO').fetchall()
for nome_coluna in lista_de_colunas:
    sql_lista_de_colunas.append(nome_coluna[3])

# validando colunas do arquivo e da tabela
if (len(obj_lista_de_colunas) != len(sql_lista_de_colunas)) | (
        sorted(obj_lista_de_colunas) != sorted(sql_lista_de_colunas)):
    validacao.append('COLUNAS INCORRETS')

# retirando aspas da lista com nome de colunas do arquivo
obj_matrix = arquivo.as_matrix()
insert_colunas = str(tuple(obj_lista_de_colunas)).replace("'", "")

# validações duplicidades
duplicidade = pd.read_sql(
    """SELECT chave_premio FROM  PRODUCAO.DBO.GESTAO_PREMIACAO A 
                WHERE A.chave_premio in """ + str(tuple(arquivo['chave_premio'])).replace(",)", ")"), cn)
if duplicidade['chave_premio'].count() != 0:
    validacao.append('Existem Duplicidades. Premio ja Imortado Chave = ' + str(
        tuple(duplicidade['chave_premio'])) + ', Arquivo Deletado')

if validacao != []:
    print(validacao)
    raise ValueError

contador = 0

# inicia validações de tranformação da dados
for i in range(qtde_linhas):
    transformando_values = []
    for x in obj_matrix[i]:
        # registros nulos
        if x == True:
            var = 1
        elif x == False:
            var = 0
        elif fnmatch(str(x), '???.???.???-??'):
            var = x.replace("-", "").replace(".", "")
        elif str(x) == 'NaT':
            var = "'**NULL**'"
        # outros
        else:
            var = x
        transformando_values.append(var)



    # criando chave
    transformando_values[10] = str(int(transformando_values[9])) + '|' + str(transformando_values[6]) + '|' + str(
        transformando_values[7]) + '|' + str(transformando_values[0])

    # tratando informaçoes da base para importacao
    insert_values = str(tuple(transformando_values)).replace("'**NULL**'", 'NULL').replace('"NULL"', 'NULL').replace(
        'nan', 'NULL').replace("Timestamp(", "").replace("))", ")")

    # mais uma validação de Desconto de Faltas
    if transformando_values[1] == transformando_values[4] and transformando_values[2] > 0 and transformando_values[
        3] > 0:
        validacao.append('Desconto de Faltas não foi Realizado')

    if validacao != []:
        print(validacao)
        raise ValueError

        # efetuando importacao no banco
    #print(f"INSERT INTO GESTAO_PREMIACAO {insert_colunas} VALUES{insert_values}")
    cursor.execute(f"INSERT INTO GESTAO_PREMIACAO {insert_colunas} VALUES {insert_values}")
    contador = contador + 1
    cursor.commit()

# validando teto
teto = arquivo['vlr_pagar']
teto = [teto]
for a in range(len(teto)):
    for z in teto[a]:
        if z >= 2000.00:
            print('Fucionarios com Valor de Premio acima de R$ 2000,00 ')

demitidos = pd.read_sql(
    """ SELECT CPF FROM  DW..V_ML_FUNCIONARIO A 
                 WHERE  SIT_EMPRE = 'DEMITIDO'    AND       A.CPF IN """ + str(tuple(arquivo['cpf'])).replace(",)",
                                                                                                              ")"), cn)
# demitidos = [demitidos]
if demitidos['CPF'].count() > 0:
    print('Foram importados ' + str(demitidos['CPF'].count()) + ' CPFs Demitidos ')

print('Foram importados ' + str(contador) + ' Premiação(ões)')

cursor.close()
cn.close()

# salvando arquivo em execel tratado LOG
nome_log = str(dtatual.strftime('%Y-%m-%d')) + ' ' + nomearq + '.xlsx'
writer = pd.ExcelWriter('N:\Planejamento\PLAN\PREMIACOES\FORMULARIOS DE PREMIACAO\LOG\\{}'.format(nome_log), engine='xlsxwriter')
arquivo.to_excel(writer, sheet_name='Sheet1')
writer.save()
print('Log salvo com o nome: {}'.format(nome_log))


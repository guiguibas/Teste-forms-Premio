from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


from .models import Tipo_Premio,Departamentos,Premio,Funcionarios


def hello(request):
    return HttpResponse('Ola Mundo')

def hello2(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi: {} '.format(str(year)))

def lerBanco(nome):
    lista_nomes = [
            {'nome' :'Ana', 'idade': 20},
            {'nome': 'Pedro', 'idade': 25},
            {'nome': 'Joaquim', 'idade': 27},
    ]

    for pessoa in lista_nomes:
            if pessoa['nome'] == nome:
                return pessoa
    else:
        return {'nome': 'Não Encontrado','idade': 0}

def tipopremio(request):
    lists = Tipo_Premio.objects.all()
    departs = Departamentos.objects.all()
    crt_custo = request.POST.get("CC_Custo")
    funcionario = Funcionarios.objects.all()
    premio = Premio.objects.all()
    return render(request, 'home.html', {'lists': lists,'departs':departs, 'crt_custo':crt_custo , 'funcionario':funcionario, 'premio':premio })

def premio_add(request):
    premio = PremioForm(request.POST or None, request.FILES or None)

    if premio.is_valid():
        premio.save()
    return render(request, 'home.html',{'premio':premio})







# Create your views here.

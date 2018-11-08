from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PersonForm,PremioForm
from .models import Person, Tipo_Premio,Departamentos,Funcionarios,Premio


def hello(resquest):
    return HttpResponse('Ola Mundo')

def hello2(resquest):
    return render(resquest, 'index.html')

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

@login_required
def person_list(request):
    persons = Person.objects.all()
    return render(request,'person.html', {'persons': persons})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return  redirect('person_list')
    return render(request, 'person_form.html',{'form': form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'form': form})

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

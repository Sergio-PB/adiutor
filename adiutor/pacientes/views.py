from django.shortcuts import render
from django.http import HttpResponse
from .models import terapeutas, pacientes

from django.contrib import messages
#messages.add_message(request, message.)

def index(request):
    return render(request, 'pacientes/index.html')

def login(request):
    name = request.POST.get('nome')
    crp = request.POST.get('crp')
    password = request.POST.get('senha')

    for terapeuta in terapeutas.objects.all():
        if name == terapeuta.Nome:
            if crp == terapeuta.Crp:
                if password == terapeuta.Senha:
                    pacients = pacientes.objects.filter(Terapeuta=terapeuta).order_by('Nome')
                    context = {'terapeuta':terapeuta, 'pacientes':pacients}
                    return render(request, 'pacientes/terapeuta.html', context)
                return render(request, 'pacientes/index.html', {'message':'Senha inválida'})
            return render(request, 'pacientes/index.html', {'message':'CRP inválido'})
    return render(request, 'pacientes/index.html', {'message':'Nome inválido'})

def acao(request):
    name = request.GET.get('nome')
    terapeuta = terapeutas.objects.get(Nome=name)
    id = request.GET.get('id')
    pacient = pacientes.objects.get(Id=id)
    context = {'terapeuta':terapeuta, 'paciente':pacient}
    return render(request, 'pacientes/acao.html', context)

#import os
#os.mkdir('teste')
def escrever(request):
    name = request.GET.get('nome')
    id = request.GET.get('id')
    pacient = pacientes.objects.get(pk=id)
    if request.method == 'POST':
        date = request.POST.get('data')
        texto = request.POST.get('texto')
        f = open(str("pacientes/prontuarios/"+id), "a+")
        f.write(str(date))
        f.write("\n"+texto+"\n\n")
        f.close()
        return render(request, 'pacientes/acao.html', context)
    context = {'nome':name, 'paciente':pacient}
    return render(request, 'pacientes/escrever.html', context)

def migrar(request):
    name = request.GET.get('nome')
    terapeuta = terapeutas.objects.get(Nome=name)
    id = request.GET.get('id')
    pacient = pacientes.objects.get(Id=id)
    if request.method == 'POST':
        escolhido = request.POST.get('escolhido')
        password = request.POST.get('senha')
        if password == terapeuta.Senha:
            pacient.Terapeuta = terapeutas.objects.get(Nome=escolhido)
            pacient.save()
            message = 'Paciente migrado com sucesso'
            pacients = pacientes.objects.filter(Terapeuta=terapeuta)
            context = {'terapeuta':terapeuta, 'pacientes':pacients, 'message':message}
            return render(request, 'pacientes/terapeuta.html', context)
        else:
            return HttpResponse("Senha incorreta")

    terapeutasPossiveis = terapeutas.objects.exclude(Nome=name)
    context = {'paciente':pacient, 'terapeuta':terapeuta, 'terapeutas':terapeutasPossiveis}
    return render(request, 'pacientes/migrar.html', context)

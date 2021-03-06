from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import terapeutas, pacientes

from django.contrib import messages
#messages.add_message(request, message.)
import codecs

def index(request):
    return render(request, 'pacientes/index.html')

def login(request):
    name = request.POST.get('nome')
    crp = request.POST.get('crp')
    password = request.POST.get('senha')

    for t in terapeutas.objects.all():
        if name == t.Username:
            if crp == t.Crp:
                if password == t.Senha:
                    #pacients = pacientes.objects.filter(Terapeuta=t).order_by('Nome')
                    context = {'terapeuta':t}
                    return redirect(('/terapeuta?nome='+str(t.Nome)))
                    #return render(request, 'pacientes/terapeuta.html', context)
                return render(request, 'pacientes/index.html', {'message':'Senha inválida'})
            return render(request, 'pacientes/index.html', {'message':'CRP inválido'})
    return render(request, 'pacientes/index.html', {'message':'Nome inválido'})

def terapeuta(request):
    name = request.GET.get('nome')
    terapeuta = terapeutas.objects.get(Nome=name)
    pacients = pacientes.objects.filter(Terapeuta=terapeuta).order_by('Nome').exclude(Status='ENCERRADO')
    context = {'terapeuta':terapeuta, 'pacientes':pacients}
    return render(request, 'pacientes/terapeuta.html', context)

def acao(request):
    if request.method == 'GET':
        name = request.GET.get('nome')
        id = request.GET.get('id')
    elif request.method == 'POST':
        name = request.POST.get('nome')
        id = request.POST.get('id')
    terapeuta = terapeutas.objects.get(Nome=name)
    pacient = pacientes.objects.get(Id=id)
    context = {'terapeuta':terapeuta, 'paciente':pacient}
    return render(request, 'pacientes/acao.html', context)

#import os
#os.mkdir('teste')
def escrever(request):
    name = request.GET.get('nome') #Essa parte nao eh do form
    terapeuta = terapeutas.objects.get(Nome=name)
    id = request.GET.get('id')
    pacient = pacientes.objects.get(pk=id)
    context = {'terapeuta':terapeuta, 'paciente':pacient}
    if request.method == 'POST':
        date = request.POST.get('data')
        texto = request.POST.get('texto')
        f = open(str("pacientes/prontuarios/"+id), "a+")
        f.write(str(date))
        f.write("\n"+texto+"\n\n")
        f.close()
        return render(request, 'pacientes/acao.html', context)
    return render(request, 'pacientes/escrever.html', context)

def ler(request):
    name = request.GET.get('nome')
    terapeuta = terapeutas.objects.get(Nome=name)
    id = request.GET.get('id')
    pacient = pacientes.objects.get(pk=id)
    f = codecs.open(str("pacientes/prontuarios/"+id), "r", encoding='utf-8')
    print(str("pacientes/prontuarios/"+id))
    text = f.read()
    f.close()
    context = {'terapeuta':terapeuta, 'paciente':pacient, 'texto':text}
    return render(request, 'pacientes/ler.html', context)

def anamnese(request):
    name = request.GET.get('nome')
    terapeuta = terapeutas.objects.get(Nome=name)
    id = request.GET.get('id')
    pacient = pacientes.objects.get(pk=id)
    context = {'terapeuta':terapeuta, 'paciente':pacient}
    if request.method == 'POST':
        password = request.POST.get('senha')
        if password == terapeuta.Senha:
            corpo = request.POST
            elementos = list(corpo)[2:-1]
            f = codecs.open(str("pacientes/prontuarios/"+id), "w+", encoding='utf-8')
            f.write("PRONTUÁRIO DE "+str(pacient)+"\n\n----------Anamnese----------\n\n")
            for elemento in elementos:
                f.write(str(elemento)+" : "+str(corpo[elemento])+"\n")
            f.write("\n\n----------Prontuários----------\n\n")
            f.close()
            pacient.Status = 'ATENDIMENTO'
            pacient.save()
            message = 'Anamnese realizada com sucesso!'
            pacients = pacientes.objects.filter(Terapeuta=terapeuta).order_by('Nome').exclude(Status='ENCERRADO')
            context = {'terapeuta':terapeuta, 'pacientes':pacients, 'message':message}
            return render(request, 'pacientes/terapeuta.html', context)
        else:
            return HttpResponse("Senha incorreta")
    return render(request, 'pacientes/anamnese.html', context)

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
            f = codecs.open(str("pacientes/prontuarios/"+id), "a+", encoding='utf-8')
            f.write("\n\n----------PACIENTE MIGRADO PARA "+str(escolhido)+"----------\n\n")
            message = 'Paciente migrado com sucesso'
            pacients = pacientes.objects.filter(Terapeuta=terapeuta).order_by('Nome').exclude(Status='ENCERRADO')
            context = {'terapeuta':terapeuta, 'pacientes':pacients, 'message':message}
            return render(request, 'pacientes/terapeuta.html', context)
        else:
            return HttpResponse("Senha incorreta")

    terapeutasPossiveis = terapeutas.objects.exclude(Nome=name)
    context = {'paciente':pacient, 'terapeuta':terapeuta, 'terapeutas':terapeutasPossiveis}
    return render(request, 'pacientes/migrar.html', context)

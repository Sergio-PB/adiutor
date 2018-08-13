from django.shortcuts import render
from django.http import HttpResponse
from .models import terapeutas, pacientes

def index(request):
    return render(request, 'pacientes/index.html')

def login(request):
    name = request.GET.get('nome')
    crp = request.GET.get('crp')
    password = request.GET.get('senha')

    for terapeuta in terapeutas.objects.all():
        if name == terapeuta.Nome:
            if crp == terapeuta.Crp:
                if password == terapeuta.Senha:
                    pacients = pacientes.objects.filter(Terapeuta=terapeuta).order_by('Nome')
                    context = {'nome':name, 'crp':crp,'senha':password, 'pacientes':pacients}
                    return render(request, 'pacientes/terapeuta.html', context)
                return HttpResponse("Senha incorreta")
            return HttpResponse("CRP incorreto")
    return HttpResponse("Nome inválido")

def acao(request):
    name = request.GET.get('nome')
    id = request.GET.get('id')
    pacient = pacientes.objects.get(Id=id)
    context = {'nome':name, 'paciente':pacient}
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

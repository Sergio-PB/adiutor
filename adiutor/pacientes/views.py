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
    status = request.GET.get('status')
    pacient = request.GET.get('paciente')
    context = {'nome':name, 'id':id, 'status':status, 'paciente':pacient}
    return render(request, 'pacientes/acao.html', context)

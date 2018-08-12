from django.shortcuts import render
from django.http import HttpResponse
from .models import terapeutas, pacientes

def index(request):
    return render(request, 'pacientes/index.html')

def login(request):
    name = request.GET.get('nome')
    crp = request.GET.get('crp')
    password = request.GET.get('senha')
    context = {'nome':name, 'crp':crp,'senha':password}
    for terapeuta in terapeutas.objects.all():
        if name == terapeuta.Nome:
            if crp == terapeuta.Crp:
                if password == terapeuta.Senha:
                    return HttpResponse("Cadastro válido")
                return HttpResponse("Senha incorreta")
            return HttpResponse("CRP incorreto")
    return HttpResponse("Cadastro inválido")

    return render(request, 'pacientes/login.html', context)

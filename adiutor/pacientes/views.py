from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pacientes/index.html')

def login(request):
    name = request.GET.get('nome')
    crp = request.GET.get('crp')
    password = request.GET.get('senha')
    context = {'nome':nome, 'crp':crp,'senha':senha}

    return render(request, 'pacientes/login.html', context)

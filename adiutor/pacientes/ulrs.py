from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('terapeuta', views.terapeuta, name='terapeuta'),
    path('acao', views.acao, name='acao'),
    path('escrever', views.escrever, name='escrever'),
    path('anamnese', views.anamnese, name='anamnese'),
    path('migrar', views.migrar, name='migrar'),
    path('ler', views.ler, name='ler'),

]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('acao', views.acao, name='acao'),
    path('escrever', views.escrever, name='escrever'),
    path('migrar', views.migrar, name='migrar'),
]

from django.urls import include, path
from .views import *


urlpatterns = [
    path('veiculo/listar/<str:categoria>/',listar_veiculo,name='listar_veiculo'),
    path('veiculo/perfil/<int:pk>/',perfil_veiculo,name='perfil_veiculo')
]
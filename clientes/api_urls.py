from django.urls import path
from . import api_views

urlpatterns = [
    path("clientes/", api_views.listar_clientes, name="api_listar_clientes"),
    path("clientes/status/", api_views.atualizar_status_cliente, name="api_atualizar_status_cliente"),
]

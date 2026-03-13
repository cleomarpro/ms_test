from django.shortcuts import render
from .models import Cliente, StatusCliente


def lista_clientes(request):
    data = {}
    id_cliente = request.GET.get("id_cliente")
    status_cliente = request.GET.get("status_cliente")
    if request.GET.get("todos_cliente"):
        data['clientes'] = Cliente.objects.all()
    else:
        data['clientes'] = Cliente.objects.filter(status=StatusCliente.ATIVO)
    if id_cliente:
        cliente = Cliente.objects.filter(id=id_cliente).first()
        if cliente:
            cliente.status = status_cliente
            cliente.save() 

    return render(request, "clientes/lista_clientes.html", data)
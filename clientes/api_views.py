
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, StatusCliente
from .serializers import ClienteSerializer


@api_view(["GET"])
def listar_clientes(request):
    """Lista clientes ativos ou todos se ?todos_cliente=on"""
    if request.GET.get("todos_cliente"):
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(status=StatusCliente.ATIVO)
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def atualizar_status_cliente(request):
    """Ativa ou inativa um cliente via POST"""
    id_cliente = request.data.get("id_cliente")
    status_cliente = request.data.get("status_cliente")

    cliente = Cliente.objects.filter(id=id_cliente).first()
    if not cliente:
        return Response({"erro": "Cliente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    cliente.status = status_cliente
    cliente.save()
    serializer = ClienteSerializer(cliente)
    return Response(serializer.data, status=status.HTTP_200_OK)

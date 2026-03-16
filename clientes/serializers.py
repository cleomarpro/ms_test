# clientes/serializers.py
from rest_framework import serializers
from .models import Cliente, StatusCliente

class ClienteSerializer(serializers.ModelSerializer):
    status_cliente = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = ["id", "nome", "email", "tipo", "status_cliente"]

    def get_status_cliente(self, obj):
        return "ATIVO" if obj.status == StatusCliente.ATIVO else "INATIVO"

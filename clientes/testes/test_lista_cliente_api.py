from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from clientes.models import Cliente, StatusCliente, TipoCliente


class ClienteApiTests(TestCase):
    def setUp(self):
        # cliente criado com id previsível
        self.cliente = Cliente.objects.create(
            id=5,  # força o ID para bater com os testes
            nome="Ana",
            email="ana@email.com",
            tipo=TipoCliente.PESSOA_FISICA,
            status=StatusCliente.ATIVO,
        )
        self.client = APIClient()

    def test_listar_clientes_ativos(self):
        resp = self.client.get(reverse("api_listar_clientes"))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(all(c["status_cliente"] == "ATIVO" for c in data))

    def test_listar_todos_clientes(self):
        resp = self.client.get(reverse("api_listar_clientes"), {"todos_cliente": "on"})
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertGreater(len(data), 0)

    def test_ativar_cliente(self):
        resp = self.client.post(reverse("api_atualizar_status_cliente"), {
            "id_cliente": self.cliente.id,
            "status_cliente": "ATIVO"
        }, format="json")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status_cliente"], "ATIVO")

    def test_inativar_cliente(self):
        resp = self.client.post(reverse("api_atualizar_status_cliente"), {
            "id_cliente": self.cliente.id,
            "status_cliente": "INATIVO"
        }, format="json")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status_cliente"], "INATIVO")

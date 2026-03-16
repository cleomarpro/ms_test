from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from clientes.models import Cliente, TipoCliente, StatusCliente


class ClienteViewsTests(TestCase):
    def setUp(self):
        self.cliente_1 = Cliente.objects.create(
            nome="Ana",
            email="ana@email.com",
            tipo=TipoCliente.PESSOA_FISICA,
            status=StatusCliente.ATIVO,
        )
        self.cliente_2 = Cliente.objects.create(
            nome="Bruno",
            email="bruno@email.com",
            tipo=TipoCliente.PESSOA_JURIDICA,
            status=StatusCliente.ATIVO,
        )

        self.cliente_ativo = Cliente.objects.create(
            nome="Maria",
            email="maria@email.com",
            tipo=TipoCliente.PESSOA_FISICA,
            status=StatusCliente.ATIVO,
        )
        self.cliente_inativo = Cliente.objects.create(
            nome="joão",
            email="joao@email.com",
            tipo=TipoCliente.PESSOA_JURIDICA,
            status=StatusCliente.INATIVO,
        )
    
    def test_inativar_cliente_via_get(self):
        self.client.get(reverse("lista_clientes"), {
            "id_cliente": self.cliente_ativo.id,
            "status_cliente": StatusCliente.INATIVO,
        })
        self.cliente_ativo.refresh_from_db()
        self.assertEqual(self.cliente_ativo.status, StatusCliente.INATIVO)

    def test_ativar_cliente_via_get(self):
        self.client.get(reverse("lista_clientes"), {
            "id_cliente": self.cliente_inativo.id,
            "status_cliente": StatusCliente.ATIVO,
        })
        self.cliente_inativo.refresh_from_db()
        self.assertEqual(self.cliente_inativo.status, StatusCliente.ATIVO)

    def test_listagem_carrega_com_status_200(self):
        response = self.client.get(reverse("lista_clientes"))
        self.assertEqual(response.status_code, 200)

    def test_listagem_exibe_tipos_dos_clientes(self):
        response = self.client.get(reverse("lista_clientes"))
        self.assertContains(response, "Pessoa Física")
        self.assertContains(response, "Pessoa Jurídica")

    def test_lista_clientes_padrao_mostra_apenas_ativos_via_get(self):
        response = self.client.get("/clientes/")
        clientes = response.context["clientes"]
        self.assertIn(self.cliente_ativo, clientes)
        self.assertNotIn(self.cliente_inativo, clientes)

    def test_lista_clientes_padrao_mostra_inativos_e_ativos_via_get(self):
        response = self.client.get("/clientes/", {"todos_cliente": "on"})
        clientes = response.context["clientes"]
        self.assertIn(self.cliente_ativo, clientes)
        self.assertIn(self.cliente_inativo, clientes)


class SeedClientesCommandTests(TestCase):
    def test_seed_cria_ao_menos_50_clientes_e_eh_idempotente(self):
        call_command("seed_clientes")
        self.assertGreaterEqual(Cliente.objects.count(), 50)

        call_command("seed_clientes")
        self.assertEqual(Cliente.objects.count(), 50)

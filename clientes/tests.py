from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import Cliente, TipoCliente


class ClienteViewsTests(TestCase):
    def setUp(self):
        self.cliente_1 = Cliente.objects.create(
            nome="Ana",
            email="ana@email.com",
            tipo=TipoCliente.PESSOA_FISICA,
        )
        self.cliente_2 = Cliente.objects.create(
            nome="Bruno",
            email="bruno@email.com",
            tipo=TipoCliente.PESSOA_JURIDICA,
        )

    def test_listagem_carrega_com_status_200(self):
        response = self.client.get(reverse("lista_clientes"))
        self.assertEqual(response.status_code, 200)

    def test_listagem_exibe_tipos_dos_clientes(self):
        response = self.client.get(reverse("lista_clientes"))
        self.assertContains(response, "Pessoa Física")
        self.assertContains(response, "Pessoa Jurídica")


class SeedClientesCommandTests(TestCase):
    def test_seed_cria_ao_menos_10_clientes_e_eh_idempotente(self):
        call_command("seed_clientes")
        self.assertGreaterEqual(Cliente.objects.count(), 10)

        call_command("seed_clientes")
        self.assertEqual(Cliente.objects.count(), 10)

from django.core.management.base import BaseCommand
from clientes.models import Cliente, TipoCliente, StatusCliente
import random

NOMES_BASE = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Kleber", "Larissa", "Marcos", "Natália", "Otávio",
    "Paula", "Ricardo", "Sofia", "Tiago", "Vanessa"
]

class Command(BaseCommand):
    help = "Cria uma massa de clientes para ambiente de desenvolvimento."

    def handle(self, *args, **options):
        criados = 0
        atualizados = 0

        # Limpa todos os clientes antes de recriar
        Cliente.objects.all().delete()

        # Gera exatamente 50 clientes
        for i in range(1, 51):
            nome = random.choice(NOMES_BASE)
            email = f"{nome.lower()}{i}@example.com"
            tipo = random.choice([
                TipoCliente.PESSOA_FISICA,
                TipoCliente.PESSOA_JURIDICA,
                TipoCliente.VIP
            ])
            status = random.choice([StatusCliente.ATIVO, StatusCliente.INATIVO])

            cliente, created = Cliente.objects.update_or_create(
                email=email,
                defaults={
                    "nome": nome,
                    "tipo": tipo,
                    "status": status,
                }
            )

            if created:
                criados += 1
            else:
                atualizados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed finalizado. Criados: {criados} | Atualizados: {atualizados}"
            )
        )

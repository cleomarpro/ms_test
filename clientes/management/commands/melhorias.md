
## Nova  Verção

Em vez de lista fixa, usa uma lista base de nomes e gera até 50 clientes.

E‑mails únicos: combina nome + índice para evitar duplicação.

Tipos e status aleatórios: cada cliente pode ser Pessoa Física, Jurídica ou VIP, e pode estar Ativo ou Inativo.

Usa update_or_create para manter o comando idempotente (não duplica se rodar várias vezes).

Resultado: uma massa de dados variada, com dezenas de clientes diferentes, útil para testar filtros, listagens e relatórios.
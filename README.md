# Teste Prático — Desenvolvedor(a) Júnior Python/Django

## 1. Objetivo do teste

Este teste tem como objetivo avaliar sua capacidade de realizar uma pequena evolução em um projeto Django já existente, de forma funcional, organizada e coerente.

No dia a dia do MB, grande parte do trabalho envolve:
- entender requisitos simples de negócio
- alterar código existente
- ajustar models, views, templates e queries
- implementar mudanças com cuidado
- validar o comportamento da funcionalidade
- explicar com clareza o que foi feito

Este teste foi pensado para simular esse tipo de cenário de forma objetiva e justa.

---

## 2. Contexto

Você recebeu um projeto Django base já funcional com um módulo de clientes.

Atualmente:
- existe um model `Cliente`
- existe uma listagem de clientes
- os clientes cadastrados aparecem normalmente na tela

Precisamos evoluir esse projeto para permitir a **inativação e reativação de clientes**, além de ajustar a listagem para respeitar essa regra.

---

## 3. Desafio

Implementar a funcionalidade de **inativação de clientes**, fazendo com que clientes inativos não apareçam na listagem padrão.

---

## 4. Requisitos obrigatórios

### 4.1. Alteração no model
1. OK - Adicionar ao model `Cliente` o campo `ativo`
2. OK  Exibir apenas clientes ativos por padrão
3. OK Permitir visualizar todos os clientes com filtro opcional
4. OK Criar forma de inativar e reativar clientes
5. OK Criar pelo menos 2 testes automatizados
6. OK Atualizar o `seed_clientes` para gerar uma massa de dados
7. Separe o backend do frontend, para boas práticas de desenvolvimento:
- O frontend será feito em um novo projeto que irá acessar as informações deste projeto;
- O frontend deve ser feito em Angular e consumir endpoints do backend;
- Pode utilizar no backend o DRF (Django Rest Framework) para criação dos endpoints;
8. A melhor solução para este teste não é a mais complexa e sim:
- a mais simples;
- a mais clara;
- a mais funcional;
- a mais organizada;
9. Ao final, atualize este README com uma seção chamada "O que foi implementado", descrevendo brevemente:
- o que você fez;
- eventuais decisões tomadas;
- qualquer observação importante sobre sua implementação;
- como rodar o projeto completo, dividido em backend e frontend.
10. Você pode utilizar IA como apoio no desenvolvimento, porém esperamos que você:
- entenda o que implementou
- consiga explicar suas escolhas
- consiga responder perguntas simples sobre o próprio código
11. Junto com a entrega faça um vídeo de no máximo 10 minutos explicando o que foi feito, junto com as envidências do software rodando.

---

## 5. Bônus inicial:

```python
## Como rodar o projeto
```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver

## 6. O que foi implementado
- descrevendo brevemente:
    

- o que você fez;
    .foi adicionado um capo de estatus  no model Cliente e no template
    . Na view foi feito o filto padrão clientes ativos e todos os clientes
    .  foi  criado um checked no template clientes que ao ser marcado ele lista todos os clientes
    . Foi criad na view clientes uma função para altera o status do cliente 
    . Foi criado no template cliente um botão para inativar e ativar o cliente

    .Foi criado 4 testes para validar a view cleinte
    sao eles:                                              test_lista_clientes_padrao_mostra_inativos_e_ativos_via_get
    test_lista_clientes_padrao_mostra_apenas_ativos_via_get
    test_ativar_cliente_via_get
    test_inativar_cliente_via_get
    . Foi atualizado o seed_clientes  para cria até 50 clientes
    . ci: validado com pytest -s (todos os testes passaram)

- eventuais decisões tomadas;
    . Foi atualizado o seed_clientes  para cria até 50 clientes
    ci: validado com pytest -s (todos os testes passaram)
- qualquer observação importante sobre sua implementação;
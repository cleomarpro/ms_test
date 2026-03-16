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
7. OK Separe o backend do frontend, para boas práticas de desenvolvimento:
- OK  O frontend será feito em um novo projeto que irá acessar as informações deste projeto;
- OK O frontend deve ser feito em Angular e consumir endpoints do backend;
- OK  Pode utilizar no backend o DRF (Django Rest Framework) para criação dos endpoints;
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
python manage.py migrate"
python manage.py runserver



## 6. O que foi implementado

## 🚀 Como rodar o projeto

### Backend (Django)
```bash
python -m venv .venv   # no Codespace já vem instalado
source .venv/bin/activate   # no Codespace já vem ativada
pip install -r requirements.txt   # no Codespace já vem instalado
python manage.py migrate   # no Codespace já migra automaticamente
python manage.py runserver
python manage.py seed_clientes # Cria clientes para testes
```

#### Executar os testes
```bash
pytest -s
python manage.py seed_clientes   # cria clientes automaticamente para testes
```

---

### Frontend (Angular)
1. Instale o **Node.js versão LTS**.  
2. Instale as dependências:
```bash
npm install @angular/cli --save-dev
npm install
```
3. Rode o servidor:
```bash
ng serve
```

---

## 🛠️ Tecnologias Utilizadas
- **Backend:** Django + Django REST Framework  
- **Frontend:** Angular  
- **Banco de Dados:** SQLite (padrão do Django, podendo ser adaptado)  
- **Testes:** Pytest  
- **Infra:** Codespaces + `.devcontainer` para dockerização  

---

## ⚙️ Funcionalidades Implementadas
- Campo **ativo** adicionado ao model `Cliente`.  
- Listagem padrão exibindo apenas clientes ativos.  
- Opção para listar **todos os clientes** via checkbox.  
- Botão para ativar/inativar clientes diretamente no template.  
- API REST com endpoints:
  - `GET /api/clientes/` → lista apenas ativos  
  - `GET /api/clientes/?todos_cliente=on` → lista todos  
  - `POST /api/clientes/status/` → ativa ou inativa cliente  
- Frontend Angular consumindo os endpoints da API.  

---

## ✅ Testes Implementados

### Testes de Views
- `test_lista_clientes_padrao_mostra_inativos_e_ativos_via_get`  
- `test_lista_clientes_padrao_mostra_apenas_ativos_via_get`  
- `test_ativar_cliente_via_get`  
- `test_inativar_cliente_via_get`  

### Testes de Endpoints
- `test_listar_clientes_ativos`  
- `test_listar_todos_clientes`  
- `test_ativar_cliente`  
- `test_inativar_cliente`  

Além disso:
- Seed atualizado para criar até **50 clientes**.  
- Todos os testes passaram com sucesso (`pytest`).  

---

## 📌 Observações
- O projeto foi estruturado para ser simples e didático, mas já contempla boas práticas de desenvolvimento.  
- A integração entre **Django REST Framework** e **Angular** garante escalabilidade e flexibilidade.  
- O código foi validado com testes automatizados, garantindo confiabilidade nas principais funcionalidades.  

---

## 🧭 Decisões Tomadas
- Atualizei o seed para criar clientes automaticamente para testes.  
- Criei testes específicos para os endpoints das API.  
- Configurei `.devcontainer` para dockerizar o projeto, garantindo execução em qualquer máquina sem erros.  
- Mantive o banco de dados **SQLite3** para simplicidade.  
- Usei **pytest** para executar e validar os testes.  

---

## 🚀 Próximos Passos
- Implementar paginação na listagem de clientes.  
- Adicionar autenticação e autorização na API e nas views.  
- Melhorar a interface do frontend no Angular.  
- Implementar mais filtros de busca.  

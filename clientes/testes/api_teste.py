import requests

BASE_URL = "http://localhost:8000/api"  # ajuste conforme seu servidor

# 1. Listar apenas clientes ativos
resp_ativos = requests.get(f"{BASE_URL}/clientes/")
print("Clientes ativos:", resp_ativos.json())

# 2. Listar todos os clientes
resp_todos = requests.get(f"{BASE_URL}/clientes/", params={"todos_cliente": "on"})
print("Todos os clientes:", resp_todos.json())

# 3. Ativar um cliente (exemplo: id=5)
resp_ativar = requests.post(f"{BASE_URL}/clientes/status/", json={
    "id_cliente": 5,
    "status_cliente": "ATIVO"
})
print("Cliente ativado:", resp_ativar.json())

# 4. Inativar um cliente (exemplo: id=5)
resp_inativar = requests.post(f"{BASE_URL}/clientes/status/", json={
    "id_cliente": 5,
    "status_cliente": "INATIVO"
})
print("Cliente inativado:", resp_inativar.json())

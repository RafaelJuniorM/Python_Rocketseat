import pytest
import requests

# URL do servidor que irá testar
BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "nova Tarefa",
        "description": "Descrição da nova tarefa"
    }

    response = requests.post(f"{BASE_URL}/tasks" ,json = new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])
    
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

def test_update_task():
    if tasks: #garante que a lista de tarefas não está vazia
        task_id = tasks[0]
        payload = { # dados que serão atualizados 
            "completed": True,
            "description": "Descrição atualizada",
            "title": "Título atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload) # encia uma requisição put para atualizar a tarefa
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json # valida se a resposta contém a chave "message"

        # Nova requisição para verificar se a tarefa foi atualizada
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json() # converte a resposta em json
        assert response_json["completed"] == payload["completed"]
        assert response_json["description"] == payload["description"]
        assert response_json["title"] == payload["title"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 404
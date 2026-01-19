from flask import Flask, request, jsonify
from models.task import Task

## __name__ = "__main__"
app = Flask(__name__)  # inicializa o Flask - instancia da aplicação - __name__  é o modulo principal da aplicação

tasks = [] # armazena todas tarefas
task_id_control = 1 # controla o ID das tarefas

# criação da rota para criar tarefas
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title = data["title"], description = data.get("description",""))
   
    task_id_control += 1
   
    tasks.append(new_task)

    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!" , "id": new_task.id})


# listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    
    output = {
               "tasks": task_list,
               "total_tasks": 0
            }
    return jsonify(output)    

# Listar tarefa por ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
        
    return jsonify({"message": "Tarefa não encontrada!"}), 404


# criando rota de uptade 
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task=None
    for t in tasks:
        if t.id == id:
            task = t
    if task == None:
        return jsonify({"message": "Tarefa não encontrada!"}), 404
    
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    return jsonify({"message": "Tarefa atualizada com sucesso!"})

# criando rota de delete
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if not task:
        return jsonify({"message": "Tarefa não encontrada!"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)


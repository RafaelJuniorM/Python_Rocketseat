from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required


app = Flask(__name__) # isntancia do Flask 
app.config['SECRET_KEY'] = "Your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"  # Configuração do banco de dados SQLite


login_manager = LoginManager()
 # instancia do SQLAlchemy
db.init_app(app)
login_manager.init_app(app)

#view Login
login_manager.login_view = 'login'  # Define a rota de login

@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(user_id)

# === ROTA DE LOGIN ===
@app.route('/login', methods=["POST"])
def login():
    # recebimento das credenciais do usuário atraves do body 
    data = request.json
    username = data.get("username")
    password = data.get("password")

    #verificação se as credenciais foram fornecidas
    if username and password: 
        #login
        user = User.query.filter_by(username=username).first() #busca o usuário no banco de dados pelo nome de usuário

        if user and user.password == password: #verifica se o usuário existe e se a senha está correta
            login_user(user)
            return jsonify({"message":"Login realizado com sucesso "})

    return jsonify({"message":"Credenciais inválidas"}), 400

# === ROTA DE LOGOUT ===
@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "logout realizado com sucesso "})

# === ROTA DE CRIAR USER === 
@app.route('/user', methods=["POST"])
def create_user():
    data = request.json
    #print(data)
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username=username, password=password, role="user") # criando um novo usuário e atribuindo os valores recebidos
        db.session.add(user) # adicionando o novo usuário à sessão do banco de dados
        db.session.commit() # salvando as alterações no banco de dados
        return jsonify({"message":"Usuário criado com sucesso"})

    return jsonify({"message":"Falha ao criar usuário"}), 400

# === ROTA DE INFORMACOES DO USUARIO ===
@app.route('/user/<int:user_id>', methods=["GET"])
@login_required
def get_info_user(user_id):
    user = User.query.get(user_id) #busca o usuário no banco de dados pelo ID, id fornecido na URL

    if user: 
        return {"username": user.username}
    
    return jsonify({"message":"Usuário não encontrado"}), 404

# === ROTA ATUALIZAR DADOS DO USUARIO ===
@app.route('/user/<int:user_id>', methods=["PUT"])
@login_required
def update_user(user_id):
    data = request.json 
    user = User.query.get(user_id)

    if user_id != current_user.id and current_user.role =="user":
        return jsonify({"message":"Operação não permitida"}), 403
    
    if user and data.get("password"): # passaword sera alterado 
        user.password = data.get("password")
        db.session.commit()
        return jsonify({"message":"Senha atualizada com sucesso"})
    
    return jsonify({"message":"Falha ao atualizar senha"}), 400

# == ROTA DE DELETAR USUARIO ==
@app.route('/user/<int:user_id>', methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)

    if current_user.role != "admin":
        return jsonify({"message":"Operação não permitida"}), 403

    if user and user.id != current_user.id:  # Impede que o usuário delete a si mesmo
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {user_id} deletado com sucesso"})
    
    return jsonify({"message":"Deleção invalida!!"}), 400


if __name__ == '__main__':
    app.run(debug=True)  # executa o servidor Flask em modo de depuração
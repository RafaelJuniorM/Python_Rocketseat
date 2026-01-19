from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required


app = Flask(__name__) # isntancia do Flask 
app.config['SECRET_KEY'] = "Your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"  # Configuração do banco de dados SQLite


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
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return jsonify({"message":"Login realizado com sucesso "})

    return jsonify({"message":"Credenciais inválidas"}), 400

# === ROTA DE LOGOUT ===
@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "logout realizado com sucesso "})




@app.route('/')
def teste():
    return "Isso é um testeeeee!!!"


if __name__ == '__main__':
    app.run(debug=True)  # executa o servidor Flask em modo de depuração
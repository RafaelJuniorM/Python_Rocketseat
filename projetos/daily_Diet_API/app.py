from flask import Flask
from database import db

# inicializar o flask 
app = Flask(__name__)

# configuração do banco de dados
app.config['SECRET_KEY'] = "Your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ORM 
db.init_app(app)

# criação das rotas 

if __name__ == "__main__":
    app.run(debug=True)
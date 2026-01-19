from database import db 
from flask_login import UserMixin


class User(db.Model, UserMixin): 
    # criando a tabela User no banco de dados
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(50), nullable = False, unique=True)
    password = db.Column(db.String(50), nullable=False)
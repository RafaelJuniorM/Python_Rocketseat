from flask import Flask, jsonify
from data.database import db
from models.payments import Payments

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

# criar pagamento
@app.route('/payments/pix', methods=['POST'])
def create_pix_payment():
    return jsonify({"message": "Pix payment created"}), 201

# confirmar pagamento - webhook
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "O pagamento foi confirmado "}), 201

# mostrar pagina de pagamento - conexao com sockets 
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento pix'

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify, request
from data.database import db
from models.payments import Payments
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

# criar pagamento
@app.route('/payments/pix', methods=['POST'])
def create_pix_payment():
    data = request.get_json()

    #validação
    if 'value' not in data:
        return jsonify({"message": "Value is required"}), 400

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment  = Payments(value = data['value'], 
                            expiration_date=expiration_date)
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "O pagamento foi criado",
                    "payment": new_payment.to_dict()}), 201











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


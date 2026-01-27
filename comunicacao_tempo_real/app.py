from flask import Flask, jsonify

app = Flask(__name__)


# Criando rotas 

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


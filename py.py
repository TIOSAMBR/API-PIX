from flask import Flask, request, jsonify, render_template
import mercadopago
import uuid

app = Flask(__name__)

# Configure sua chave de acesso Mercado Pago
sdk = mercadopago.SDK("APP_USR-5256639034659263-082713-2da3af28199a46ef31ab449d6e70e66c-680374983")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    
    print("Dados recebidos do formulário:", data)

    try:
        transaction_amount = float(data['transaction_amount'])
        if transaction_amount <= 0:
            return jsonify({"error": "O valor deve ser positivo"}), 400
    except ValueError:
        return jsonify({"error": "Valor inválido para 'transaction_amount'"}), 400

    payment_data = {
        "transaction_amount": transaction_amount,
        "description": data['description'],
        "payment_method_id": "pix",
        "payer": {
            "email": data['email'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "identification": {
                "number": data['identification_number']
            }
        }
    }

    print("Dados de pagamento enviados para API:", payment_data)

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': str(uuid.uuid4())
    }

    payment_response = sdk.payment().create(payment_data, request_options)
    payment = payment_response['response']

    print("Resposta Completa da API:", payment)

    if 'point_of_interaction' in payment and 'transaction_data' in payment['point_of_interaction']:
        return jsonify({
            "qr_code_base64": payment['point_of_interaction']['transaction_data']['qr_code_base64'],
            "qr_code": payment['point_of_interaction']['transaction_data']['qr_code']
        })
    else:
        return jsonify({"error": "Não foi possível gerar o código QR", "detalhes": payment}), 400

if __name__ == '__main__':
    app.run(debug=True)

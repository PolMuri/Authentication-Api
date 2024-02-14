from flask import Flask, request, jsonify, url_for
from register import add_user, is_valid_email, generate_token

app = Flask(__name__)

# Definició de la ruta per registrar usuaris mitjançant una sol·licitud POST, al ser una API hem 
# d'obligar a que només vagi per POST
@app.route('/api/register/', methods=['POST'])
def register_user():
    # Obtenir les dades del cos de la sol·licitud POST en format JSON
    data = request.get_json()

    # Comprovar si el paràmetre 'email' està present a les dades rebudes
    if 'email' not in data:
        return jsonify({"error": "Missing email parameter"}), 400

    # Obtenir l'adreça de correu electrònic de les dades rebudes
    email = data['email']

    # Comprovar si l'adreça de correu és vàlida
    if is_valid_email(email):
        # Generar un token d'autenticació
        token = generate_token()

        # Afegir l'usuari i el token a la base de dades
        add_user(email, token, 'db.json')

        # Retornar una resposta amb l'email i el token generat
        return jsonify({"email": email, "token": token}), 200
    else:
        # Retornar una resposta d'error si l'adreça de correu no és vàlida
        return jsonify({"error": "Invalid email"}), 400

# Executar l'aplicació si aquest fitxer s'està executant com a script principal
if __name__ == '__main__':
    app.run(debug=True)



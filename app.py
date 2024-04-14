from flask import Flask, request, jsonify, url_for, render_template, redirect
from register import add_user, is_valid_email, generate_token
from init import initialize_password
from login import login
from verify import verify_token

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
    
# Definició d'una nova ruta per la inicialització de contrasenya
@app.route('/api/init/', methods=['POST'])
def init_password():
    # Obtenir les dades del cos de la sol·licitud POST en format JSON
    data = request.get_json()

    # Verificar si els paràmetres 'token' i 'password' són presents a les dades rebudes
    if 'token' not in data or 'password' not in data:
        return jsonify({"error": "Missing token or password parameter"}), 400

    # Obtenir el token i la contrasenya de les dades rebudes
    token = data['token']
    password = data['password']

    # Inicialitzar la contrasenya utilitzant la funció importada d'init.py
    initialize_password(token, password)

    # Retornar una resposta
    return jsonify({"message": "Password initialized successfully"}), 200

# Definició d'una nova ruta per a l'inici de sessió de l'usuari 
@app.route('/api/login', methods=['POST'])
def user_login():
    # Obtenció de les dades JSON de la sol·licitud POST
    data = request.get_json()
    # Obtenció de l'adreça electrònica (email) i la contrasenya de les dades rebudes
    email = data.get('email')
    password = data.get('password')

    # Comprovació de si es proporciona l'email i la contrasenya
    if not email or not password:
        # Si algun dels dos camps falta, es retorna un error
        return jsonify({"error": "Email and password are required"}), 400

     # Intent d'iniciar sessió amb les credencials proporcionades
    token = login(email, password)
    if token:
        # Si les credencials són vàlides, es retorna un token d'autenticació amb un codi d'estat HTTP 200
        return jsonify({"token": token}), 200
    else:
        # Si les credencials no són vàlides, es retorna un missatge d'error amb un codi d'estat HTTP 401
        return jsonify({"error": "Invalid email or password"}), 401
    
# Ruta per verificar un token
@app.route('/api/verify', methods=['POST'])
def verify_token_route():
    # Obtenir les dades JSON de la sol·licitud POST
    data = request.get_json()
    # Obtenir el token de les dades rebudes
    token = data.get('token')

    if not token:
        # Si no es proporciona el token, retornar un error amb un codi d'estat 400
        return jsonify({"error": "Token is required"}), 400

    # Verificar el token utilitzant la funció verify_token
    result = verify_token(token)

    # Verificar si és un diccionari i conté una clau 'error'
    if isinstance(result, dict) and 'error' in result:
        # Si resulta conté un error, retornar aquest error amb un codi d'estat 400
        return jsonify(result), 400
    else:
        # Si resulta no conté un error, retornar el resultat de la verificació del token
        return jsonify(result)


# Ruta per mostrar el formulari
@app.route('/formulari')
def mostrar_formulari():
    return render_template('register.html')

# Ruta per mostrar la pàgina d'índex
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gracies')
def gracies():
    success = request.args.get('success')
    email = request.args.get('email')
    token = request.args.get('token')  # Obtener el token de los argumentos de la URL
    return render_template('gracies.html', success=success, email=email, token=token)

# Ruta per mostrar el formulari d'inicialització de contraseña
@app.route('/init', methods=['GET'])
def init_form():
    return render_template('init.html')

# Ruta per mostrar el formulari d'inici de sessió
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Ruta per mostrar el formulari de verificació del token 
@app.route('/verify', methods=['GET'])
def verify_form():
    return render_template('verify.html')


# Executar l'aplicació si aquest fitxer s'està executant com a script principal
if __name__ == '__main__':
    app.run(debug=True)
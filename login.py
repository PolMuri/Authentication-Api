import json
import hashlib
import binascii
import argparse
from Crypto.PublicKey import RSA
import os
import secrets
import core



def generate_keys_if_not_exist():
    if not os.path.exists("pem"):
        os.makedirs("pem")
    if not os.path.exists("pem/private.pem") or not os.path.exists("pem/public.pem"):
        # Generar claus si no existeixen
        key = RSA.generate(2048)

        private_key = key.export_key()
        with open("pem/private.pem", "wb") as file_out:
            file_out.write(private_key)

        public_key = key.publickey().export_key()
        with open("pem/public.pem", "wb") as file_out:
            file_out.write(public_key)

# Executa aquesta funció al principi del teu script
generate_keys_if_not_exist()

# Funció per carregar la base de dades des d'un fitxer JSON (db.json)
def load_database():
    try:
        with open('db.json', 'r') as file:
            data = json.load(file)
             # Comprovar si hi ha una clau 'users' a les dades carregades
            if 'users' in data:
                # Retornar la llista d'usuaris si existeix
                return data['users']
            else:
                # Si no es troba la clau 'users', mostrar un missatge d'error i retornar una llista buida
                print('Error: No es pot trobar la llista d\'usuaris en el fitxer JSON.')
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        # En cas d'error de fitxer no trobat o error de decodificació JSON, retornar una llista buida
        return []


def validate_password(email, password, database):
    # Iterar sobre cada usuari a la base de dades
    for user in database:
        # Comprovar si l'email de l'usuari coincideix amb l'email proporcionat
        if user['email'] == email:
            # Obtenir el salt emmagatzemat al db.json
            salt = user['salt']  
            # Generar el hash de la contrasenya proporcionada utilitzant PBKDF2
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
            # Comprovar si el hash generat coincideix amb el hash emmagatzemat a la base de dades
            if password_hash == user['hash']:
                # Retornar True si la contrasenya coincideix
                return password_hash == user['hash']
    # Si no es troba cap usuari amb l'email proporcionat, retornar False        
    return False

# Funció principal
def login(email, password):
    # Generar claus si no existeixen
    generate_keys_if_not_exist()
    # Carregar la base de dades
    database = load_database()
    # Comprovar si la base de dades és una llista
    if not isinstance(database, list):
        print('Error: No es pot llegir la base de dades o no està en format JSON.')
        return

    # Validar la contrasenya
    if validate_password(email, password, database):
        # Crear un token JWT si la contrasenya és vàlida
        token = core.createBearer(email)
        return token
    else:
        return None
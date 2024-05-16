import json
import os
import re

# Aquesta funció carrega les dades des d'un fitxer JSON si aquest existeix o crea un diccionari buit si no existeix.
def load_data(db_file):
    if os.path.exists(db_file):
        with open(db_file, 'r') as f:
            data = json.load(f)
    else:
        data = {"users": []}
    return data

# Aquesta funció desa les dades en un fitxer JSON.
def save_data(data, db_file):
    with open(db_file, 'w') as f:
        json.dump(data, f, indent=4)

# Aquesta funció comprova si una adreça de correu electrònic és vàlida utilitzant una expressió regular.
def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

# Aquesta funció afegeix un usuari amb una adreça de correu i un token al fitxer de base de dades.
def add_user(email, token, db_file):
    # Comprovem si l'adreça de correu és vàlida.
    if not is_valid_email(email):  
        print("L'adreça d'email no és vàlida.")
        return

    # Carreguem les dades del fitxer json.
    data = load_data(db_file)  
    # Creem un diccionari amb les dades de l'usuari.
    user_data = {"email": email, "token": token} 
    # Afegim les dades de l'usuari a la llista d'usuaris. 
    data["users"].append(user_data) 
    # Desem les dades actualitzades al fitxer de base de dades json. 
    save_data(data, db_file) 
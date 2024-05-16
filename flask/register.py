import base64
import secrets
from db import add_user, is_valid_email  # Importa la funció "is_valid_email" des de "db.py".

# Funció per generar un token d'autenticació aleatori.
def generate_token():
    # Genera 32 bytes aleatoris per al token.
    token_bytes = secrets.token_bytes(32) 
    # Converteix els bytes aleatoris en una cadena URL-segura de 32 caràcters. 
    token = base64.urlsafe_b64encode(token_bytes).decode('utf-8')[:32]  
    return token  

# Modifica el codi per utilitzar l'adreça de correu passada com a argument.
def register_user(email):
    # Comprova si l'adreça de correu és vàlida abans de generar el token i afegir-lo a la base de dades.
    if is_valid_email(email):
        # Genera un token d'autenticació cridant la funció "generate_token".
        token = generate_token()  
        # Afegeix l'usuari i el token a la base de dades utilitzant la funció "add_user".
        add_user(email, token, 'db.json') 
        # Retorna el token generat.
        return token  
    else:
        # Retorna un missatge d'error si l'adreça de correu no és vàlida.
        return "L'adreça d'email no és vàlida."

# No utilitzem la variable email aquí.
# email = "exemple@example.com"
# Cridem aquesta funció amb l'adreça de correu obtinguda de la sol·licitud HTTP POST a l'app.py.
# Exemple d'ús:
# result = register_user(adreca_de_correu_obtinguda)
# print(result)




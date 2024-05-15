# Importem les funcions necessàries d'altres fitxers
from core import update_user_token
from db import load_data, save_data

# Definim la ruta de la BD
rutaDB = "db.json"

# Definim una funció per inicialitzar la contrasenya
def initialize_password(token, password):
    # Carreguem les dades actuals de la BD
    data = load_data(rutaDB)
    # Actualitzem la informació de l'usuari amb el token i la contrasenya proporcionats
    update_user_token(data, token, password)
    # Desem les dades actualitzades a la base de dades
    save_data(data, rutaDB)

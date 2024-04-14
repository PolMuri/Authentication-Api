# Importa las funciones necesarias de otros archivos
from core import update_user_token
from db import load_data, save_data

# Define la ruta de la base de datos
rutaDB = "db.json"

# Define una función para inicializar la contraseña
def initialize_password(token, password):
    # Carga los datos actuales de la base de datos
    data = load_data(rutaDB)
    # Actualiza la información del usuario con el token y la contraseña proporcionados
    update_user_token(data, token, password)
    # Guarda los datos actualizados en la base de datos
    save_data(data, rutaDB)

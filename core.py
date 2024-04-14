import hashlib
import secrets
import json
from datetime import datetime, timedelta, timezone

def update_user_token(data, token, password):
    # Funció per actualitzar la informació d'un usuari en base al token i contrasenya proporcionats.
    for user in data["users"]:
        if user["token"] == token:
            user["token"] = None
            salt = secrets.token_hex(20)
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
            user["hash"] = password_hash.hex()
            user["salt"] = salt

# Importació de mòduls de la llibreria jwt
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

def crearBearer (mail):
    # Funció per crear un token JWT (JSON Web Token) a partir de l'adreça de correu.
    instance = JWT()

    message = {
        'mail': mail,
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(hours=1)),
    }

    # Codifica el missatge com a JWT (JWS).
   
    # O carrega una clau RSA des d'un fitxer PEM.
    with open('pem/private.pem', 'rb') as fh:
        signing_key = jwk_from_pem(fh.read())
    # També es pot carregar una clau octet de la mateixa manera que la clau RSA.
    # signing_key = jwk_from_dict({'kty': 'oct', 'k': '...'})

    compact_jws = instance.encode(message, signing_key, alg='RS256')
    return compact_jws
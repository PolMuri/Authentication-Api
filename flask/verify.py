from jwt import JWT, jwk_from_pem
import json

def verify_token(bearer_token):
    # Funció per verificar un token Bearer i mostrar el missatge (payload) del JWT.
    with open('pem/public.pem', 'rb') as fh:
        verifying_key = jwk_from_pem(fh.read())

    instance = JWT()
    try:
        # Intenta decodificar el token utilizant la clau pública.
        decoded_token = instance.decode(bearer_token, verifying_key, do_time_check=True)

        # Verifica si el token decodificat és None o si sla seva longitud és 0
        if decoded_token is None or len(decoded_token) == 0:
            return {"error": "Error verifying token: decoded token is invalid"}
        
        # Si el token és vàlid el tornem
        return decoded_token
    except Exception as e:
        # En caso d'error, mostra un missatge d'error.
        return {"error": f"Error verifying token: {e}"}

# Crida la funció verify_token si s'executa el fitxer com script principal
# només ho necessitem si cridem el codi directament
#if __name__ == "__main__":

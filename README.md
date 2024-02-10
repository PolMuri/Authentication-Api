Preparar i aixecar l'API Flask del register:


## Configuració Inicial  

1. **Clonar el Repositori:**   
     ```git clone <url_del_repositori.git>  cd <nom_del_directori>`

2. **Instal·lar Dependències:**

    
    `pip install -r requirements.txt`
    
3. **Configurar la Base de Dades:**
    
    - Podeu utilitzar un script o eines específiques per inicialitzar o configurar la base de dades segons les necessitats.

## Execució de l'API

4. **Aixecar l'API Flask:**
    
    bashCopy code
    
    `python app.py`
    
    L'API estarà disponible a `http://127.0.0.1:5000/`.

## Provar l'API

5. **Registrar un Usuari:**
    
    
    `curl -X POST -H "Content-Type: application/json" -d '{"email": "example@email.com"}' http://127.0.0.1:5000/api/register/`
    
    Això retornarà un token i registrarà l'usuari a la base de dades.
    
    Es pot cercar l'usuari registrat al fitxer db.json creat de forma automàtica si no existeix ja aquest fitxer que actua com a BD.

## Estructures del Projecte

- **app.py:** Fitxer principal que defineix l'aplicació Flask i les rutes.
- **register.py:** Lògica del registre amb funcions com `generate_token`, `is_valid_email`, i `add_user`.
- **db.py:** Funcions relacionades amb la base de dades com `load_data`, `save_data`, `is_valid_email`, i `add_user`.

## Nota

Assegura't de tenir Python i les eines requerides instal·lades a l'entorn abans d'executar l'API.
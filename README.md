Preparar i aixecar l'API Flask del register:


## Configuració Inicial  

1. **Clonar el Repositori:**   
     ```git clone <url_del_repositori.git>  cd <nom_del_directori>`
    
2. **Configurar la Base de Dades:**
    
    - Podeu utilitzar un script o eines específiques per inicialitzar o configurar la base de dades segons les necessitats.

## Execució de l'API

1. **Aixecar l'API Flask:**
    
    bashCopy code
    
    `python app.py`
    
    L'API estarà disponible per defecte a `http://127.0.0.1:5000/`.

## Provar l'API

1. **Registrar un Usuari:**

    -Permet registrar nous usuaris proporcionant la seva adreça de correu electrònic.

    -Genera un token d'autenticació únic per a cada usuari registrat.

    -Emmagatzema la informació dels usuaris, incloent-hi el seu correu electrònic i el token, en un fitxer de base de dades db.json.
    
    ```
    curl -X POST -H "Content-Type: application/json" -d '{"email": "example@email.com"}' http://127.0.0.1:5000/api/register/
    ```
    Això retornarà un token i registrarà l'usuari a la base de dades.
    
    Es pot cercar l'usuari registrat al fitxer db.json creat de forma automàtica si no existeix ja aquest fitxer que actua com a BD.

2. **Inicialitzar Contrasenya:**

    -Permet inicialitzar les contrasenyes per als usuaris existents.

    -Cerca un usuari pel seu token i guarda un hash segur de la contrasenya proporcionada a db.json.

    ```
    curl -X POST -H "Content-Type: application/json" -d '{"token": "token", "password": "password"}' http://127.0.0.1:5000/api/init/
    ```
    Això inicialitzarà la contrasenya de l'usuari associat amb el token proporcionat.

3. **Iniciar Sessió:**

    -Facilita el procés d'inici de sessió pels usuaris registrats.

    -Genera un token d'autorització (Bearer token) per a l'usuari proporcionat, permetent l'accés a recursos protegits.

    ```
    curl -X POST -H "Content-Type: application/json" -d '{"email": "example@email.com", "password": "password"}' http://127.0.0.1:5000/api/login
    ```
    Això iniciarà la sessió de l'usuari amb l'email i la contrasenya proporcionats.

4. **Verificar Token:**

    -Permet verificar un token d'autorització JWT i mostrar el seu contingut (payload).

    -Requereix la clau pública associada a la clau privada utilitzada durant el procés d'inici de sessió.

    ```
    curl -X POST -H "Content-Type: application/json" -d '{"token": "token"}' http://127.0.0.1:5000/api/verify
    ```
    Això verificarà el token proporcionat i mostrarà el contingut (payload) del JWT si és vàlid.

## Estructures del Projecte

- **app.py:** Fitxer principal que defineix l'aplicació Flask i les rutes.
- **register.py:** Lògica del registre amb funcions com `generate_token`, `is_valid_email`, i `add_user`.
- **db.py:** Funcions relacionades amb la base de dades com `load_data`, `save_data`, `is_valid_email`, i `add_user`.
- **init.py**: Funcions relacionades amb la inicialització de contrasenya com `initialize_password`.
- **login.py:** Funcions relacionades amb l'inici de sessió com `login` i `validate_password`.
- **verify.py:** Conté la funció per verificar un token JWT `verify_token`.

## Nota

Assegura't de tenir Python i les eines requerides instal·lades a l'entorn abans d'executar l'API.



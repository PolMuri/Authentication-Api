# api

# Aplicació Flask d'exemple amb "Hello World"

Aquest repositori conté una aplicació senzilla "Hello World" amb Flask.

## Preparar l'entorn

1. **Instal·lar Flask:**
   ``pip install Flask``

## Executar l'aplicació

Clonar el repositori:

``git clone git@github.com:PolMuri/api.git``
``cd api``

Crear una nova branca (opcional):

``git checkout -b helloworld``

Executar l'aplicació:

``flask --app hello run``

## Accedir a l'aplicació:

Obrir un navegador i anar a http://127.0.0.1:5000/ o a l'adreça que ens surti per pantalla

## Exemple de Codi de hello world amb flask

Aquí tens un exemple senzill de codi per a la teva aplicació:


```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

## Aturar l'aplicació

Prem "Ctrl + C" a la terminal on s'està executant Flask.
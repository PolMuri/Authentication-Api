#Usa la imatge oficial de Python com a base
FROM python:3.8-alpine

# Afegeix les eines de compilació necessàries
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    make

#Estableix el directori de treball
WORKDIR /app

#Copia el fitxer requirements.txt al directori de treball
COPY ./requirements.txt /app/requirements.txt

#Instal·la les dependències de Python
RUN pip3 install -r requirements.txt

#Copia el contingut de la carpeta 'flask' al directori de treball
COPY flask/ .

#Exposa el port 5000 del contenidor
EXPOSE 5000

#Crea un volum per contenir el fitxer 'db.json'
VOLUME /data

#Executa la comanda per iniciar l'aplicació Flask
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]

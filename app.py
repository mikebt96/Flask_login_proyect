#Estas librerías me permiten convertir mi PC en un servidor web
from flask import Flask
from flask_restful import Resource, Api
from rutas import RutasApi #Importo la clase RutasApi que contiene las rutas de mi servidor web

#Estamos creando una instancia/objeto de flask  (se importa la clase Resource y la clase Api)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

#El objeto "app" es el que me va a permitir manejar el servidor web
# Instancia/objeto de API(flask_restful)
api = Api(app)
#Me va a permitir controloar los recursos que voy a exponer en mi servidor


rutas = RutasApi() #Creo una instancia/objeto de la clase RutasApi
rutas.inicializar_rutas(api) #Inicializo las rutas en el objeto api

#Levantamos el servidor web
app.run(debug=True, port=8000)
#debug=True: cada vez que yo haga un cambio en el código, el servidor se reinicia automáticamente
#Le indica que va a ser puro desarrollo y no será una aplicación real

#port=8000: el puerto por el cual va a estar escuchando mi servidor web

#Al final se debe poner cada cosa en archivos diferentes
#Se debe buscar la atomización del código



# Direccion IPv4 local 192.168.0.19

from recursos import *

#Creamos una clase que me permita manejar las rutas

class RutasApi:
    #Recibe el lugar donde estaran disponibles las rutas

    def inicializar_rutas(self, api):
        # api.add_resource(HelloWorld, '/') #Le estoy diciendo que el recurso HelloWorld va a estar disponible en la ruta raíz del servidor
        # api.add_resource(HelloWorld, '/hola') #Le estoy diciendo que el recurso HelloWorld va a estar disponible en la ruta /hola del servidor
        api.add_resource(InicioDeSesion, '/login') #Le estoy diciendo que el recurso InicioDeSesion va a estar disponible en la ruta /login del servidor

        api.add_resource(RegistroUsuario, '/signup') #Le estoy diciendo que el recurso RegistroUsuario va a estar disponible en la ruta /signup del servidor



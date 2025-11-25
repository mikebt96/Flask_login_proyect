from flask_restful import Resource
from flask import make_response, render_template, request
import os

#Creamos un recurso/resource (Recurso: a lo que un usuario puede acceder en el servidor)
#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'} #Lo que retorna el método es lo que va a ver el usuario

#Todo recurso que se cree va a estar representado por una clase
#Todo recurso que se cree debe tener una dirección, en otras palabras una ruta

def cleanscreen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

class InicioDeSesion(Resource):
    def get(self):
        return make_response(render_template('login.html'))
    
    def post(self):
        print ("---------- LA INFORMACIÓN SE ESTÁ PROCESANDO ----------")

        email = request.form.get("email")
        password = request.form.get("password")

        print(f'Correo: {email}')
        print(f'Password: {password}')

        return "Procesando inicio de sesion..."

class RegistroUsuario(Resource):
    
    def get(self):
        return make_response(render_template('signup.html'))
    
    def post(self):
        cleanscreen()
        print (f"---------- LA INFORMACIÓN SE ESTÁ PROCESANDO ----------\n")

        name_signup = request.form.get("name")
        phone = request.form.get("phone")
        email_signup = request.form.get("email")
        password_signup = request.form.get("password")
        password_verification = request.form.get("password-verify")
        terms = request.form.get("terms")

        print(f"""
Se registró el usuario:         {name_signup}

Con correo:                     {email_signup}

Teléfono:                       {phone}""")
        print(f"""
Contraseña:                     {password_signup}""")
        print(f"""
Verificación de contraseña:     {password_verification}""")
        print(f"""
Terminos y Condiciones:         {terms}""""\n")

        return "Procesando registro de usuario..."
from email import message
from flask import Flask, render_template, request, jsonify, redirect
import baseDatos
import hashlib

def principal():
    return render_template('index.html')

def logear():
    return render_template('login.html')

def registrar():
    return render_template('register.html', message=0)

def cartelera():
    return render_template('billboard.html', message1=0)

def contactar():
    return render_template('contact.html')

def confirmarRegistro():
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    identification = request.form.get('identification')
    email = request.form.get('email')
    password = request.form.get('password')
    retorno = baseDatos.consultaEspecifica(email, "")
    if len(retorno) == 0:    
        verificacion = baseDatos.insertRecord(name, lastname, identification, email, password)
        if verificacion == 1:
            return render_template('confirmation.html', message=1)
        
        else:
            return render_template('confirmation.html', message=5)            
    else:
        return render_template('confirmation.html', message=0)

def confirmarSesion():
    user = request.form.get('user')
    password = request.form.get('password')
    results = baseDatos.consultaEspecifica(user, password)
    if len(results) != 0:
        pass_encrip = hashlib.sha256(password.encode('utf-8'))
        pass_encrip_hex = pass_encrip.hexdigest()
        if pass_encrip_hex == results[0][4]:  
            return render_template('billboard.html', message1=results[0][0], message2=results[0][2], message3=results[0][3])
        else:
            return render_template('confirmation.html', message=3)
    else:
        return render_template('confirmation.html', message=4)

def prepararDatos():  
    results = baseDatos.consultaEspecifica(request.get_json(), "")   
    message = {'name': results[0][0],
                'lastname': results[0][1],
                'identification': results[0][2],
                'email': results[0][3],
                'password':results[0][4]}
    return jsonify(message)

def obtenerDatos(name, lastname, identification, email, password):
    print(name, lastname, identification, email, password)
    return render_template('register.html', message=1, message1=name, message2=lastname, message3=identification, message4=email, message5=password)

def actualizarRegistro():
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    identification = request.form.get('identification')
    email = request.form.get('email')
    password = request.form.get('password')
    print(name, lastname, identification, email, password)
    baseDatos.update(name, lastname, identification, email, password)
    return render_template('confirmation.html', message=2)

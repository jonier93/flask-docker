from flask import Flask, render_template, request, redirect, jsonify
from server import app
from controllers.controlador import principal, logear, registrar, cartelera, contactar, confirmarRegistro, confirmarSesion, prepararDatos, obtenerDatos, actualizarRegistro
import json

@app.route('/')
@app.route('/home')
def func1():
    return principal()

@app.route('/login')
def func2():
    return logear()

@app.route('/register')
def func3():
    return registrar()

@app.route('/billboard')
def func4():
    return cartelera()

@app.route('/contact')
def func5():
    return contactar()

@app.route('/createUser', methods=['post'])
def func6():
    return confirmarRegistro()

@app.route('/loginData', methods=['post'])
def func7():
    return confirmarSesion()

@app.route('/datos', methods=['POST'])
def func8():    
    return prepararDatos()

@app.route('/actualizar/<name>/<lastname>/<identification>/<email>/<password>') # Método GET
def func9(name, lastname, identification, email, password): #es obligatorio colocar el argumento, de lo contrario botará error
    return obtenerDatos(name, lastname, identification, email, password)

@app.route('/actualizarRegistro', methods=['post'])
def func10():    
    return actualizarRegistro()
    
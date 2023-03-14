import sqlite3
import hashlib

connection = sqlite3.connect('baseCine.db', check_same_thread=False)
cursor = connection.cursor()

def insertRecord(nombre, apellido, cedula, correo, contrasena):
    try:
        print(nombre, apellido, cedula, correo, contrasena)
        pass_encrip = hashlib.sha256(contrasena.encode('utf-8'))
        pass_encrip_hex = pass_encrip.hexdigest()
        instruccion = "INSERT INTO clientes VALUES ('" +  nombre + "', '" + apellido + "', " + cedula + ", '" + correo +  "', '" + pass_encrip_hex + "');"
        cursor.execute(instruccion) # se envía la instrucción a SQLite
        connection.commit() # Se utiliza para confirmar que queremos guardar los datos
        return 1
    except sqlite3.Error as error:
        print(str(error))
        return 0

def consultaEspecifica(usuario, contrasena):
    try:        
        instruccion = "SELECT * FROM clientes WHERE email = '" + usuario + "';"
        cursor.execute(instruccion)
        results = cursor.fetchall()  
        return results
    except sqlite3.Error as error:
        print(str(error))

def update(name, lastname, identification, email, password):
    try:
        instruccion = "UPDATE clientes SET name = '" + name + "', lastname = '" + lastname + "', email = '" + email + "', password = '" + password + "' WHERE cedula = " + identification + ";"
        print(instruccion)
        cursor.execute(instruccion)
        connection.commit()
    except sqlite3.Error as error:
        print(str(error))




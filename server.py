from flask import Flask, render_template
import baseDatos
import os
from pathlib import Path
 
static_path = os.path.join(os.getcwd(), 'frontend/static').replace('\\', '/')
template_path = os.path.join(os.getcwd(), 'frontend/templates').replace('\\', '/')

app = Flask(__name__, static_url_path='', static_folder=static_path, template_folder=template_path)

from routes.rutas import * #Debe ir después de declarar app, ya que app es usado en este módulo que se está importando

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)

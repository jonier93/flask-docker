from flask import Flask, render_template
import baseDatos
import os
from pathlib import Path
from settings import AppSettings
#from dotenv import load_dotenv

static_path = os.path.join(os.getcwd(), 'frontend/static').replace('\\', '/')
template_path = os.path.join(os.getcwd(), 'frontend/templates').replace('\\', '/')

app = Flask(__name__, static_url_path='', static_folder=static_path, template_folder=template_path)

from routes.rutas import * #Debe ir después de declarar app, ya que app es usado en este módulo que se está importando

if __name__ == '__main__':
    """dotenv_path = Path("local-setting.env")
    load_dotenv(dotenv_path)"""
    port = int(os.environ.get('PORT', AppSettings.PORT_DEPLOY))
    host = os.environ.get('SERVER_HOST', '0.0.0.0')
    app.run(host, port)

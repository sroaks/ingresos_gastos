from flask import Flask
#Instanciar la aplicacion
app = Flask(__name__)
#este import tiene que ir aquí.
from registro_ig.routes import *

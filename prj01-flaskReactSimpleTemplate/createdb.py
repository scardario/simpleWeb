import os
from flask import Flask, render_template, request, json
from models import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Una manera de inicializar el app, la otra es db = SQLAlchemy(app)
db.init_app(app)

def main():
	db.create_all()

def agregarUsuarioPrueba():
	usuario = Usuario(nombre="Mameluco")
	db.session.add(usuario)
	db.session.commit()


if __name__ == "__main__":
	with app.app_context():
		main()
		agregarUsuarioPrueba()
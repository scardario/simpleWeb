import os
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Una manera de inicializar el app, la otra es db.init(app)
db = SQLAlchemy(app)

@app.route("/")
def indice():
	usuarios = Usuario.query.all()
	return render_template("index.html", usuarios=usuarios)

@app.route("/login")
def login():
	# cosas = list(request.environ.keys())
	# session['cosa'] = 'algo'
	# cosas = list(session.items())
	# print(cosas)

	return render_template("login.html")

@app.route("/accionLogin", methods=["POST"])
def accionLogin():
	# request.form solo sirve para POST, session guarda cualquier variable en forma de diccionario
	""" cosas = list(request.form.items())
	otrasCosas = list(session.items())
	print(cosas, otrasCosas) """

	nombre = request.form.get("campoNombre")
	usuario = Usuario.query.filter_by(nombre=nombre).first()
	if usuario is None:
		return render_template("mensaje.html", tituloMensaje="Error", mensaje="No se encuentra usuario en la base de datos")
	else:
		session['usuarioActivo']=nombre
		return render_template("account.html", nombre=nombre)

@app.route("/registro")
def registro():
	return render_template("signup.html")

@app.route("/accionRegistro", methods=["POST"])
def accionRegistro():
	nombre = request.form.get("campoNombre")
	nuevoUsuario = Usuario(nombre=nombre)
	db.session.add(nuevoUsuario)
	try:
		db.session.commit()
	except:
		return render_template("mensaje.html", tituloMensaje="Error", mensaje="No se pudo agregar usuario")
	return render_template("mensaje.html", tituloMensaje="Usuario agregado", mensaje="Se acaba de agregar a {} al sistema".format(nombre))
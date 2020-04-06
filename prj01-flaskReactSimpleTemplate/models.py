from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
	__tablename__="usuarios"
	id=db.Column(db.Integer, primary_key=True)
	nombre=db.Column(db.String, nullable=False, unique=True)

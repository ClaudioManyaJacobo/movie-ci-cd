from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pelicula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)

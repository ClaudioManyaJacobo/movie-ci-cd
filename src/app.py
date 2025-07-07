from flask import Flask, render_template, request, redirect, url_for
from model import db, Pelicula

def create_app(config=None):
    app = Flask(__name__)

    # ✅ Config por defecto
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peliculas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ✅ Si recibo config de test, la sobreescribo
    if config:
        app.config.update(config)

    db.init_app(app)

    @app.before_request
    def create_tables():
        db.create_all()

    @app.route('/')
    def index():
        peliculas = Pelicula.query.all()
        return render_template('index.html', peliculas=peliculas)

    @app.route('/add', methods=['GET', 'POST'])
    def add():
        if request.method == 'POST':
            titulo = request.form['titulo']
            director = request.form['director']
            pelicula = Pelicula(titulo=titulo, director=director)
            db.session.add(pelicula)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add.html')

    return app

# Solo para correr directamente
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

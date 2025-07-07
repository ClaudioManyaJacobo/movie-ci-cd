import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import create_app, db, Pelicula

@pytest.fixture
def client():
    test_db_path = os.path.join(os.path.dirname(__file__), 'test.db')

    config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{test_db_path}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    app = create_app(config)
    client = app.test_client()

    with app.app_context():
        db.create_all()
        pelicula = Pelicula(titulo="Interestelar", director="Christopher Nolan")
        db.session.add(pelicula)
        db.session.commit()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    if os.path.exists(test_db_path):
        os.remove(test_db_path)


def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Interestelar' in rv.data

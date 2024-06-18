import pytest
from app import create_app, db
from app.models import User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    testing_client = flask_app.test_client()

    with flask_app.app_context():
        db.create_all()
        yield testing_client
        db.drop_all()


def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Personal Health Dashboard!" in response.data

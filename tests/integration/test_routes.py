import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from tutorial5.website import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()


def test_login_page_loads(client):
    response = client.get('/login')
    assert response.status_code == 200


def test_signup_page_loads(client):
    response = client.get('/sign-up')
    assert response.status_code == 200


def test_register_user(client):
    response = client.post('/sign-up', data={
        'email': 'test@test.com',
        'username': 'testuser',
        'password1': 'password123',
        'password2': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_login_invalid(client):
    response = client.post('/login', data={
        'email': 'wrong@test.com',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_home_page(client):
    response = client.get('/')
    assert response.status_code in [200, 302]
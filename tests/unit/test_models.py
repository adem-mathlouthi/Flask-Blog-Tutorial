import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from tutorial5.website import create_app, db
from tutorial5.website.models import User, Post, Comment, Like


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


def test_create_user(app):
    with app.app_context():
        user = User(email="test@test.com", username="testuser", password="hashed")
        db.session.add(user)
        db.session.commit()
        assert User.query.count() == 1


def test_user_fields(app):
    with app.app_context():
        user = User(email="adem@test.com", username="adem", password="hashed")
        db.session.add(user)
        db.session.commit()
        u = User.query.first()
        assert u.email == "adem@test.com"
        assert u.username == "adem"


def test_create_post(app):
    with app.app_context():
        user = User(email="test@test.com", username="testuser", password="hashed")
        db.session.add(user)
        db.session.commit()
        post = Post(text="Hello world", author=user.id)
        db.session.add(post)
        db.session.commit()
        assert Post.query.count() == 1


def test_create_comment(app):
    with app.app_context():
        user = User(email="test@test.com", username="testuser", password="hashed")
        db.session.add(user)
        db.session.commit()
        post = Post(text="Hello world", author=user.id)
        db.session.add(post)
        db.session.commit()
        comment = Comment(text="Nice post!", author=user.id, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        assert Comment.query.count() == 1


def test_create_like(app):
    with app.app_context():
        user = User(email="test@test.com", username="testuser", password="hashed")
        db.session.add(user)
        db.session.commit()
        post = Post(text="Hello world", author=user.id)
        db.session.add(post)
        db.session.commit()
        like = Like(author=user.id, post_id=post.id)
        db.session.add(like)
        db.session.commit()
        assert Like.query.count() == 1
from app import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ім’я = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    пароль = db.Column(db.String(100), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    назва = db.Column(db.String(100), nullable=False)
    автор = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), unique=True, nullable=False)
    категорія_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    автор_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    категорія = db.Column(db.String(100), nullable=False)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    автор = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
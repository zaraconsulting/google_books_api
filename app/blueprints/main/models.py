from flask_sqlalchemy import SQLAlchemy
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String, unique=True)
    title = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f'<Books: {self.title} | {self.author} | {self.publisher}>'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    book_id = db.Column(db.String)
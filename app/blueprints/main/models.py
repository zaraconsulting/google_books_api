from flask_sqlalchemy import SQLAlchemy
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f'<Books: {self.title} | {self.author} | {self.publisher}>'
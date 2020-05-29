from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_,and_

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True} # Create table if not existe
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String, nullable =False)
    password = db.Column(db.String, nullable =False)

class Books(db.Model):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True} # Create table if not existe
    id = db.Column(db.Integer, primary_key =True)
    isbn = db.Column(db.String, nullable =False)
    title = db.Column(db.String, nullable =False)
    author = db.Column(db.String, nullable =False)
    year = db.Column(db.Integer, nullable =False)


class Reviews(db.Model):
    __tablename__ = "reviews"
    __table_args__ = {'extend_existing': True} # Create table if not existe
    id = db.Column(db.Integer, primary_key =True)
    book_id = db.Column(db.Integer, db.ForeignKey("Books.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    comment = db.Column(db.String, nullable =True)
    rating = db.Column(db.Integer, nullable =True)
import os,json,csv
from flask import Flask, render_template
from models import *

# export FLASK_APP=application.py. On Windows, 
# the command is instead set FLASK_APP=application.py
# you may optionally want to set the environment variable FLASK_DEBUG = 1
# flask run
app = Flask(__name__)
# Check for environment variable
os.environ["DATABASE_URL"] = "postgres://ptkcyeofdytfbx:9786bd7a9ffac6480fc0fd481bd9a8f1c03609adf7bae421b7eee8c25a9e1b9e@ec2-3-211-48-92.compute-1.amazonaws.com:5432/dalrn9safle7dt"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") # Database location
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db.init_app(app) # Database with app

def init_db(): # Create every class as table from models
    print("Tables creating...")
    return db.create_all()

def fill_db():
    f = open (".data/books.csv")
    reader = csv.reader(f)
    next(reader)
    for isbn , title, author, year in reader:
        book = Books(isbn = isbn,title = title,author = author,year = year )
        db.session.add(book)
    db.session.commit()

# Link the Flask app with the database (no Flask app is actually being run yet).

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context(): # when u are allow to interact. Interact in the command line
        init_db()
        fill_db()
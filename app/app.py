import os
from flask import Flask, render_template, request
from create import *

app = Flask(__name__)
os.environ["DATABASE_URL"] = "postgres://ptkcyeofdytfbx:9786bd7a9ffac6480fc0fd481bd9a8f1c03609adf7bae421b7eee8c25a9e1b9e@ec2-3-211-48-92.compute-1.amazonaws.com:5432/dalrn9safle7dt"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_DEBUG"] = 1

db.init_app(app)

@app.route("/login", methods=['POST',"GET"])
def login():
    if request.method == "POST":
        username = password = ""
        username = request.form.get("username")
        password = request.form.get("password")
        user = None
        user = Users.query.filter(and_(Users.username == username),(Users.password == password)).first()
        if user:
            books = Books.query.order_by(Books.author).all()
            return render_template("books.html",books = books[:100])
        else:
            return render_template("error.html", messsage = "Error user")
    else:
        return render_template("login.html")

@app.route("/register", methods=['POST',"GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        book = Users(username = username,password = password)
        db.session.add(book)
        db.session.commit()
        return render_template("login.html")
    else:
        return render_template("register.html", message="Error username")

#res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "HHbKhvgaoyPvmlLacoUxMQ", "work_reviews_count": "9781632168146"})
@app.route("/books", methods=['POST',"GET"])
def books():
    if request.method == "GET": # None in [author,title,isbn]:
        books = Books.query.order_by(Books.author).all()
    elif request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        isbn = request.form["isbn"]
        books = Books.query.filter(and_(Books.author.like(f"%{author}%"),Books.title.like(f"%{title}%"),Books.isbn.like(f"%{isbn}%"))).order_by(Books.author).all()
    return render_template("books.html",books = books[:100])

@app.route("/book/<int:book_id>", methods=["GET"]) # Default value methods is GET
def book(book_id):
    """List details about a single flight."""
    # Make sure flight exists.
    book = Books.query.get(book_id)
    if book is None:
        return render_template("error.html", message="No such flight.")
    # Get all passengers.
    return render_template("book.html", book=book)
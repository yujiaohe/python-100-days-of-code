from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# CRUD - create, read, update, delete

# create a new database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test-books-collection.db"
db = SQLAlchemy(app)

# create a new table
with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.String(250), nullable=False)


    db.create_all()

# create a new record
with app.app_context():
    try:
        # primary key id is optional, will be auto-generated
        new_book = Book(id=1,
                        title="Harry Potter",
                        author="J. K. Rowling",
                        rating=9.3
                        )
        db.session.add(new_book)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

# read all records
with app.app_context():
    all_books = db.session.query(Book).all()

# read a particular record by query
with app.app_context():
    book = Book.query.filter_by(title="Harry Potter").first()

# Update a particular record by query
with app.app_context():
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# update a record by primary key
with app.app_context():
    book_id = 1
    book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter"
    db.session.commit()

# delete a particular record by primary key
with app.app_context():
    book_id = 1
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

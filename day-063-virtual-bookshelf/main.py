from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        def __repr__(self):
            return f"<Book {self.title}>"


    db.create_all()


# sqlite3 create tabel and insert data
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL,"
# #                "rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# books store in list
# all_books = []

@app.route('/')
def home():
    # book store in list
    # return render_template("index.html", books=all_books)
    return render_template("index.html", books=Book.query.all())


@app.route("/add", methods=["POST", "GET"])
def add():
    # book_form = BookForm()
    if request.method == "POST":
        # book_dict = {'title': request.form['title'],
        #              'author': request.form['author'],
        #              'rating': request.form['rating']
        #              }
        # all_books.append(book_dict)
        with app.app_context():
            book = Book(title=request.form['title'],
                        author=request.form['author'],
                        rating=request.form['rating']
                        )
            db.session.add(book)
            db.session.commit()
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    with app.app_context():
        book_to_update = db.get_or_404(Book, id)
        if request.method == "POST":
            print(request.form['rating'])
            book_to_update.rating = request.form['rating']
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", book=book_to_update)


@app.route('/delete')
def delete():
    id = request.args.get('id')
    with app.app_context():
        book_to_delete = db.get_or_404(Book, id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

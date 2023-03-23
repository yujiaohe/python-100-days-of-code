from flask import Flask
from markupsafe import escape

app = Flask(__name__)
# print(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


# Different routes using the app.route decorator
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<iframe src="https://giphy.com/embed/YRVP7mapl24G6RNkwJ" width="200" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {escape(name)}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

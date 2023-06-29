import random
from flask import Flask

random_num = random.randint(0, 10)
print(random_num)

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/b0zkcFuPGTum4gci29" width="480" height="270" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'




@app.route("/<int:number>")
def check(number):
    if number < random_num:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_num:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)

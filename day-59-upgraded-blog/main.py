from flask import Flask, render_template
import requests

app = Flask(__name__)
data = requests.get("https://api.npoint.io/096f3bbcaa998faa2229")
all_blogs = data.json()


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def get_post(num):
    print(num)
    post = all_blogs[num-1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

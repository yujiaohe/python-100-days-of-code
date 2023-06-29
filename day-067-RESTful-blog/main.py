from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

# Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONFIGURE TABLE
with app.app_context():
    class BlogPost(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        subtitle = db.Column(db.String(250), nullable=False)
        date = db.Column(db.String(250), nullable=False)
        body = db.Column(db.Text, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        img_url = db.Column(db.String(250), nullable=False)


    db.create_all()


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    post_form = CreatePostForm()
    if request.method == "POST" and post_form.validate_on_submit():
        today = datetime.today()
        new_blog = BlogPost(title=post_form.title.data,
                            subtitle=post_form.subtitle.data,
                            date=today.strftime("%B %d, %Y"),
                            body=post_form.body.data,
                            author=post_form.author.data,
                            img_url=post_form.img_url.data
                            )
        with app.app_context():
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form, message_heading="New Post")


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    with app.app_context():
        post = db.get_or_404(BlogPost, post_id)
        post_form = CreatePostForm(title=post.title,
                                   subtitle=post.subtitle,
                                   img_url=post.img_url,
                                   author=post.author,
                                   body=post.body
                                   )
        if request.method == "POST" and post_form.validate_on_submit():
            post.title = post_form.title.data
            post.subtitle = post_form.subtitle.data
            post.body = post_form.body.data
            post.author = post_form.author.data
            post.img_url = post_form.img_url.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post_id))
    return render_template("make-post.html", form=post_form, message_heading="Edit Post")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    with app.app_context():
        post_to_delete = db.get_or_404(BlogPost, post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

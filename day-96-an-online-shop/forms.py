from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, FloatField, URLField
from wtforms.validators import DataRequired, Email, URL


class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = EmailField("Email:", validators=[Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("LOGIN!")

class ProductForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    price = FloatField("Price: ", validators=[DataRequired()])
    img_url = URLField("Image_url: ", validators=[DataRequired()])
    submit = SubmitField("Add")
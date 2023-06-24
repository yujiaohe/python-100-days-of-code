"""Using what you have learnt by building the blog website using Flask,
you're now going to build your own eCommerce website. Your website needs to have a working cart and checkout.
It should be able to display items for sale and take real payment from users.
It should have login/registration authentication features.
Here is an example website:
https://store.waitbutwhy.com/
You should consider using the Stripe API:
https://stripe.com/docs/payments/checkout"""

import os
from flask import Flask, redirect, render_template, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import stripe
from product import StripeProduct
from forms import RegisterForm, LoginForm, ProductForm
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dalkfem%^8kjdfafndm#%CDfkjdnfein'

# config Bootstrap
Bootstrap(app)

# config stripe
stripe.api_key = os.getenv("API_KEY")

# config db
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# config login
login_manager = LoginManager()
login_manager.init_app(app)


# config DB tables
class User(UserMixin, db.Model):
    """
    For authentication(login,logout), inherit from UserMixin,
    which provides default implementations for all of these properties and methods.
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)


# config DB tables
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    prod_id = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String(250))


# config DB tables
class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    prod_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    prod_name = db.Column(db.String(250), nullable=False)
    prod_price = db.Column(db.Float, nullable=False)
    prod_img = db.Column(db.String(250))
    qty = db.Column(db.Integer, nullable=False)


# create DB
with app.app_context():
    db.create_all()


def cart_count():
    """query for number of items in cart"""
    if current_user.is_authenticated:
        user_carts = Cart.query.filter_by(buyer_id=current_user.id).count()
    else:
        user_carts = 0
    return user_carts


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('index.html', all_prods=products, counts=cart_count())


@login_manager.user_loader
def load_user(user_id):
    """user_loader callback used to reload the user object from the user id stored in the session,
    return None if user id is invalid
    """
    return db.session.get(User, user_id)


def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(current_user)
        if current_user.get_id() != '1':
            return abort(403)
        return f(*args, **kwargs)

    return wrapper


@app.route('/add_product', methods=['GET', 'POST'])
@admin_only
def add_product():
    prod_form = ProductForm()
    if prod_form.validate_on_submit():
        name = prod_form.name.data
        product = Product.query.filter_by(name=name).first()
        if product:
            flash("Product already exist.")
        else:
            # Register on Stripe first
            stripe_product = StripeProduct(name, prod_form.price.data, prod_form.img_url.data)
            prod_id = stripe_product.register_new_stripe()
            # Add to DB
            new_prod = Product(name=name,
                               prod_id=prod_id,
                               price=prod_form.price.data,
                               img_url=prod_form.img_url.data
                               )
            db.session.add(new_prod)
            db.session.commit()
            flash("Product is added successfully!")
            render_template('add_product.html', form=ProductForm())
    return render_template('add_product.html', form=prod_form, counts=cart_count())


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        if User.query.filter_by(email=email).first():
            flash("You've ready signed up with that email, login instead!")
            return redirect(url_for('login'))
        else:
            hashed_pw = generate_password_hash(
                register_form.password.data,
                method="pbkdf2:sha256",
                salt_length=8
            )
            new_user = User(
                email=email,
                password=hashed_pw,
                name=register_form.name.data
            )
            with app.app_context():
                db.session.add(new_user)
                db.session.commit()
                # authenticate the use with Flask-Login
                login_user(new_user)
                return redirect(url_for('home'))
    return render_template('register.html', form=register_form, counts=cart_count())


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if not user:
            flash("That email doesn't exist, please try again.")
        elif not check_password_hash(user.password, login_form.password.data):
            flash("Password incorrect, please try again.")
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form=login_form, counts=cart_count())


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/about')
def about():
    return render_template('about.html', counts=cart_count())


@app.route('/add_to_cart')
def add_to_cart():
    prod_id = request.args.get('prod_id')
    user_id = current_user.id
    user_cart = Cart.query.filter_by(buyer_id=user_id, prod_id=prod_id).first()
    if user_cart:
        user_cart.qty = + 1
        db.session.commit()
    else:
        prod = Product.query.filter_by(prod_id=prod_id).first()
        new_cart = Cart(buyer_id=user_id,
                        prod_id=prod_id,
                        prod_name=prod.name,
                        prod_price=prod.price,
                        prod_img=prod.img_url,
                        qty=1)
        db.session.add(new_cart)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/success')
def success():
    session = stripe.checkout.Session.retrieve(request.args.get('session_id'))
    # print(session)
    user_id = current_user.id
    for item in session.list_line_items():
        data_to_delete = Cart.query.filter_by(buyer_id=user_id, prod_id=item.price.id).all()
        for d in data_to_delete:
            db.session.delete(d)
        db.session.commit()
    return render_template('success.html', counts=cart_count())


@app.route('/cancel')
def cancel():
    return render_template('cancel.html', counts=cart_count())


def cart_to_list(cart_data):
    data = []
    for item in cart_data:
        data.append({'price': item.prod_id,
                     'quantity': item.qty,
                     'adjustable_quantity':
                         {
                             'enabled': True,
                         }
                     })
    return data


@app.route('/checkout')
def checkout():
    if current_user.is_authenticated:
        user_id = current_user.id
        user_cart = Cart.query.filter_by(buyer_id=user_id).all()
        line = cart_to_list(user_cart)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line,
                mode='payment',
                success_url="http://127.0.0.1:5000/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url="http://127.0.0.1:5000/cancel",
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)
    else:
        flash("Please login to add to cart.")
        return redirect("index.html")


if __name__ == '__main__':
    app.run(debug=True)

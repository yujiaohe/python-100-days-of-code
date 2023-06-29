import flask
import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

URL = "https://api.openbrewerydb.org/v1/breweries/"
types = ['', 'micro', 'nano', 'regional', 'brewpub', 'large',
         'planning', 'bar', 'contract', 'proprietor', 'closed']

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "ksjafiefa$5a@3kfjaff..sdfke124"


class QueryForm(FlaskForm):
    name = StringField("Name:")
    brewery_type = SelectField("Brewery type:", choices=types, )
    city = StringField("City: ")
    state = StringField("State/Province: ")
    country = StringField("Country: ")
    postal = StringField("Postal: ")
    submit = SubmitField("Submit")


@app.route("/")
def home():
    response = requests.get(url=f"{URL}random")
    random_data = response.json()[0]
    return render_template("index.html", brewery=random_data)


@app.route("/search", methods=["GET", "POST"])
def search():
    form = QueryForm()
    if form.validate_on_submit():
        params = {}
        keys = list(form.data.keys())[:-2]
        for key in keys:
            if form.data[key]:
                params["by_" + key] = form.data[key]
        response = requests.get(url=URL, params=params)
        print(params)
        if not params:
            flask.flash("No field was defined, result is a random list.")
        data = response.json()
        return render_template("search.html", form=form, data=data)
    return render_template("search.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

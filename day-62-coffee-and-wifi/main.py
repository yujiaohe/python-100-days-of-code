from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g.8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g.5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField('Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_rating = SelectField('Power Outlet Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

    # [('0', '✘'), ('1', '☕️'), ('2', '☕️☕️'), ('3', '☕️☕️☕️'), ('4', '☕️☕️☕️☕️'), ('5', '☕️☕️☕️☕️☕️')]
    # [('0', '✘'), ('1', '💪'), ('2', '💪💪'), ('3', '💪💪💪'), ('4', '💪💪💪💪'), ('5', '💪💪💪💪💪')]
    # [('0', '✘'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌')]

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if request.method == "POST" and form.validate_on_submit():
        data = []
        for item in form:
            if item.name not in ['submit', 'csrf_token']:
                data.append(item.data)
        print(data)
        with open("cafe-data.csv", "a") as csv_file:
            csv_file.write(f"\n{','.join(data)}")

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

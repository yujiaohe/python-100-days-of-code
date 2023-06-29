import os
from flask import Flask, render_template, request
import requests
import smtplib

GMAIL = os.getenv("GMAIL")
GMAIL_PW = os.getenv("GMAIL_PASSWORD")

app = Flask(__name__)
data = requests.get("https://api.npoint.io/096f3bbcaa998faa2229")
all_blogs = data.json()


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    message = "Contact Me"
    if request.method == "POST":
        form_data = request.form
        print(form_data["name"])
        print(form_data["email"])
        print(form_data["phone"])
        print(form_data["message"])
        message = "Successfully sent your message"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=GMAIL, password=GMAIL_PW)
            connection.sendmail(from_addr=GMAIL,
                                to_addrs=GMAIL,
                                msg=f"Subject:New Message\n\n"
                                    f"Name: {form_data['name']}\n"
                                    f"Email: {form_data['email']}\n"
                                    f"Phone: {form_data['phone']}\n"
                                    f"Message: {form_data['message']}")

    return render_template("contact.html", message_heading=message)


@app.route("/post/<int:num>")
def get_post(num):
    print(num)
    post = all_blogs[num - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

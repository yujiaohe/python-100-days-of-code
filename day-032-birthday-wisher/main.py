import random
import pandas as pd
import datetime as dt
import smtplib
import os

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(rows.month, rows.day): rows for _, rows in data.iterrows()}
# print(birthdays_dict)

now = dt.datetime.now()
today_month = now.month
today_day = now.day
if (today_month, today_day) in birthdays_dict:
    name = birthdays_dict[(today_month, today_day)]["name"]
    recipient_email = birthdays_dict[(today_month, today_day)]["email"]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        content = file.read().replace("[NAME]", name)
        print(content)
    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"Subject: Happy Birthday!\n\n{content}")
        print("email sent")



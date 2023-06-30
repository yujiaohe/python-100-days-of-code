import smtplib
import time
import os
import requests
from datetime import datetime

MY_LAT = 30.65984
MY_LNG = 104.10194

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    print(iss_latitude)

    if MY_LNG - 5 < iss_longitude < MY_LNG + 5 and MY_LAT-5 < iss_latitude < MY_LAT + 5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)
    time_now = datetime.now()
    time_hour = time_now.hour
    if time_hour >= sunset or time_hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look up👆\n\nThe ISS is above you in the sky!"
            )





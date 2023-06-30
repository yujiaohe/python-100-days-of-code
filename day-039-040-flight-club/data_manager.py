import os
import requests

ENDPOINT = os.environ.get("SHEETY_FLIGHT")
AUTH = os.environ.get("SHEETY_FLIGHT_AUTH")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        header = {
            "Authorization": AUTH
        }
        response = requests.get(url=F"{ENDPOINT}/prices", headers=header)
        print(response.text)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_iata(self):
        header = {
            "Authorization": AUTH
        }
        for city in self.destination_data:
            put_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{ENDPOINT}/prices/{city['id']}", json=put_data, headers=header)
            print(response.text)

    def add_user(self, first_name, last_name, email):
        header = {
            "Authorization": AUTH
        }
        post_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=f"{ENDPOINT}/users", json=post_data, headers=header)
        print(response.status_code)
        if response.status_code == 200:
            print("Success! Your email has been added, look forwards")
        else:
            print(response.text)

    def subscribe_user(self):
        print("Welcome to Jianguo's Flight Club.")
        print("We find the best flight deals and email you.")
        first_name = input("What is your first name?\n").title()
        last_name = input("What is your last name?\n").title()
        continue_flag = True
        while continue_flag:
            email = input("What is your email?\n")
            email_again = input("Type your email again.\n")
            if email == email_again:
                continue_flag = False
            else:
                print("Different emails, please type again.")
        self.add_user(first_name, last_name, email)
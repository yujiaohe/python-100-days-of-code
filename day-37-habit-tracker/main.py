import requests
from datetime import datetime
import os

# key in USERNAME, TOKEN, GPAPH_ID with your own
USERNAME = os.environ["ENV_USER_NAME"]
TOKEN = os.environ["ENV_TOKEN"]
GRAPH_ID = "graph1"


# ==================create user account - 1 time use==========================
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ====================create a graph definition - 1 time use================
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ====================post value to graph - can overwrite================
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
# print(today)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# ====================update value to graph================
# yesterday = datetime(year=2023, month=3, day=2).strftime("%Y%m%d")
# print(yesterday)
#
# pixel_update_endpoint = f"{pixel_creation_endpoint}/{yesterday}"
#
# pixel_update_data = {
#    "quantity": "10",
# }

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# response.raise_for_status()
# print(response.text)

# ====================delete value to graph================
# pixel_delete_endpoint = f"{pixel_creation_endpoint}/{yesterday}"
#
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
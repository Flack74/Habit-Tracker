import requests
from datetime import datetime
import os

# Retrieve environment variables for authentication
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPHID = os.environ.get("GRAPHID")

# Pixela endpoint for user creation
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment to create a new Pixela user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Pixela endpoint for graph creation
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "Hour",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment to create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixela endpoint for creating a new pixel
pixela_creation_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

# Prompt user for time spent coding
time_spend = input("How much time did you spend coding: ")

today = datetime.now()
yesterday = datetime(year=2024, month=7, day=15)

pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": time_spend,
}

# Uncomment to create a new pixel
# response = requests.post(url=pixela_creation_endpoint, json=pixel_creation_config, headers=headers)
# print(response.text)

# Format yesterday's date
yesterday_formatted = yesterday.strftime("%Y%m%d")

# Update pixel endpoint for today or any specific date
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

pixel_updation_config = {
    "quantity": time_spend,
}

# Update pixel for the given date
response = requests.put(url=update_pixel_endpoint, json=pixel_updation_config, headers=headers)
print(response.text)

# Delete pixel endpoint
delete_pixel_endpoint = update_pixel_endpoint

# Uncomment to delete the pixel for the given date
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)

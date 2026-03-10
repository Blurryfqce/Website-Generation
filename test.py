message = input("User:  ")

#Sending a POST request to the Flask app
import requests
import numpy as np
data = {
    "message": message,
    "session_id": " " #Input random alphanumeric value here as user id 
}
response = requests.post("http://127.0.0.1:5000/build", json= data)

print(response.json())

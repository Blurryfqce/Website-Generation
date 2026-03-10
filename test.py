message = input("User:  ")

#Sending a POST request to the Flask app
import requests
import numpy as np
data = {
    "message": message,
    "session_id": " " #Input random alphanumeric value here as user id 
}
response = requests.post("https://website-generator-s8u3.onrender.com/build", json= data)

print(response.json())

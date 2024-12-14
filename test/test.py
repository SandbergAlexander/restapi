import requests

url = "http://127.0.0.1:8000/user/Alexander"


response = requests.request("POST", url)

print(response.text)
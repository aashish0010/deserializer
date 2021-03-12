import requests
import json

URL = "http://127.0.0.1:8000"

data = {
    'name' : 'mohit',
    'email' : 'pudasainiaashish2@gmail.com',
    'phone' : '9810333916',
    'password' : 'aashish12'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)

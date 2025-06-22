import requests
import json

data = {"features": [63,1,145,233,1,2,150,0,2.3,0,0,1,3]}

url = "http://127.0.0.1:8888/predict/"

data = json.dumps(data)

response = requests.post(url, data)

print(response.json())
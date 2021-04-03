import json
import requests

car = {'brand': 'Toyota', 'electric': False, 'year': 2020, 'colors': ['red', 'white', 'blue']}

# dumps(): Serialize obj to a JSON formatted string
carJson = json.dumps(car, indent=2, sort_keys=True)
print(carJson)

# dump(): Serialize obj as a JSON formatted stream to fp
with open('../FILES/car.json', 'w') as file:
    json.dump(car, file, indent=2)

# loads(): Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.
car = json.loads(carJson)
print(car)

# load(): Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object.
with open('../FILES/car.json', 'r') as file:
    car = json.load(file)
    print(car)

#  Using Requests: ********************************************************************************************
# sites:
# https://jsonplaceholder.typicode.com/
# https://docs.python-requests.org/en/master/

response = requests.get('https://jsonplaceholder.typicode.com/users')
# print(response.ok) // True
# print(response.status_code) // 200
# print(response.headers['Content-Type'])  # application/json; charset=utf-8
# print(response.headers.get('content-type'))  # application/json; charset=utf-8

# Response in json format
users_json = response.json()

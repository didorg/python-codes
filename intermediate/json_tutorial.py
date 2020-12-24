import json

car = {'brand': 'Toyota', 'electric': False, 'year': 2020, 'colors': ['red', 'white', 'blue']}

# dumps(): Serialize obj to a JSON formatted string
carJson = json.dumps(car, indent=4, sort_keys=True)
print(carJson)

# dump(): Serialize obj as a JSON formatted stream to fp
with open('../FILES/car.json', 'w') as file:
    json.dump(car, file, indent=4)

# loads(): Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.
car = json.loads(carJson)
print(car)

# load(): Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object.
with open('../FILES/car.json', 'r') as file:
    car = json.load(file)
    print(car)

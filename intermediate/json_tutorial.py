import json

car = {'brand': 'Toyota', 'electric': False, 'year': 2020, 'colors': ['red', 'white', 'blue']}

# dumps(): Serialize obj to a JSON formatted string
carJson = json.dumps(car, indent=4, sort_keys=True)
print(carJson)

# dump(): Serialize obj as a JSON formatted stream to fp
with open('../FILES/car.json', 'w') as file:
    json.dump(car, file)

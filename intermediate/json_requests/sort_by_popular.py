import json


def custom_sort(pck):
    return pck['analytics']['30d']


# load(): Deserialize fp (a .read()-supporting file-like object containing a JSON document) to a Python object.
with open('../../FILES/package_info.json', 'r') as file:
    data = json.load(file)

# List Comprehension to filter the data based on certain criteria
# pck_info = [item for item in pck_info if 'library' in item['desc']]
data = [item for item in data if 20 <= item['analytics']['30d']]

# Sorting by 30d in library
data.sort(key=custom_sort, reverse=True)
pck_info_str = json.dumps(data, indent=2)
print(pck_info_str)

import json
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')
pack_json = r.json()

pack_str = json.dumps(pack_json, indent=2)
print(pack_str)


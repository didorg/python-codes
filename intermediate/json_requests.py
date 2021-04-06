import json
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()
# pack_str = json.dumps(packs_json, indent=2)
first_package = json.dumps(packages_json[0], indent=2)
pack_name = packages_json[0]['name']
pack_desc = packages_json[0]['desc']
pack_url = f"https://formulae.brew.sh/api/formula/{pack_name}.json"

# For particular package
response = requests.get(pack_url)
package_json = response.json()
print(type(package_json))
first_package_str = json.dumps(package_json, indent=2)
print(first_package_str)

installs_30 = package_json['analytics']['install_on_request']['30d'][pack_name]
installs_90 = package_json['analytics']['install_on_request']['90d'][pack_name]
installs_365 = package_json['analytics']['install_on_request']['365d'][pack_name]

print('********************************')
print(pack_name, pack_desc, installs_30, installs_90, installs_365)




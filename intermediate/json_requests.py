import json
import requests
import time

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

count = 0
data_results = []
for package in packages_json:
    # pack_str = json.dumps(packs_json, indent=2)
    pack_name = package['name']
    pack_desc = package['desc']
    pack_url = f"https://formulae.brew.sh/api/formula/{pack_name}.json"

    # For particular package
    response = requests.get(pack_url)
    package_json = response.json()
    # print(type(package_json))
    # first_package_str = json.dumps(package_json, indent=2)
    # print(first_package_str)

    installs_30 = package_json['analytics']['install_on_request']['30d'][pack_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][pack_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][pack_name]

    data = {
        'name': pack_name,
        'desc': pack_desc,
        'analytics': {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365
        }

    }

    data_results.append(data)
    time.sleep(response.elapsed.total_seconds())
    count += 1
    # Just 5 time for test
    if count >= 5:
        break

# dump(): Serialize obj as a JSON formatted stream to fp
with open('../FILES/package_info.json', 'w') as file:
    json.dump(data_results, file, indent=2)

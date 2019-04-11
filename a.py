import json

with open('repos1') as f:
    jsons = json.loads(f.read().strip())
    for j in jsons:
        print(j['full_name'])
        print(j['html_url'])
        print(j['description'])
        print("\n")

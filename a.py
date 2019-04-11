import json
import glob

files = glob.glob('./repos*')

for afile in files:
    with open(afile) as f:
        jsons = json.loads(f.read().strip())
        for j in jsons:
            print(j['full_name'])
            print(j['html_url'])
            print(j['description'])
            print("\n")

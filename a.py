import json

for i in [1,2,3,4,5,6,7]:
  with open('repos%d' % i) as f:
    jsons = json.loads(f.read().strip())
    for j in jsons:
        print(j['full_name'])
        print(j['html_url'])
        print(j['description'])
        print("\n")

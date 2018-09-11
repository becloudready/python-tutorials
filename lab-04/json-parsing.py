import json

with open("ec2.json") as f:
    content = f.read()

j = json.loads(content)

print json.dumps(j,sort_keys=True,indent=4)


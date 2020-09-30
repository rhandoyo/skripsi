import json

file_json=open("latihan.json")

data = json.loads(file_json.read())

print(data)
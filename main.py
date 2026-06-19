# outputs the data from json file which stores data
import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))
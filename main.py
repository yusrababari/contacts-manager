
import json  #outputs json file which stores data
import jmespath #jmespath used to search through data


with open('data.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))#outputs json file which stores data
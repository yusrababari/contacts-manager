# https://medium.com/toyota-connected-india/a-gentle-introduction-to-jmespath-an-intuitive-way-to-parse-json-documents-daa6d699467a - json tutorial
import json      # outputs json file which stores data
import jmespath  # jmespath used to search through data


with open('data.json', 'r') as file:
    data = json.load(file)

results = jmespath.search('contacts[?age > `20`].[firstName, lastName]', data)

names = [f"{first} {last}" for first, last in results]# loops through results and combines each first and last name into a single string

print(names)

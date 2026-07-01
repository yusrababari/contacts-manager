# https://medium.com/toyota-connected-india/a-gentle-introduction-to-jmespath-an-intuitive-way-to-parse-json-documents-daa6d699467a - json tutorial

import json      # outputs json file which stores data
import jmespath  # jmespath used to search through data using 'python -m pip install jmespath'
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")



@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")

@app.route("/api/run", methods=["POST"])
def run_script():
    data = request.get_json()
    user_input = data.get("input", "")
    result = process_data(user_input)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

with open('data.json', 'r') as file: # r means read-only
    data = json.load(file)

#results = jmespath.search('contacts[?age > `20`].[firstName, lastName]', data)# searches through contacts and returns the first and last name of anyone older than 20

#names = [f"{first} {last}" for first, last in results]# loops through results and combines each first and last name into a single string

#print(names)

results = jmespath.search('contacts[?age > `20`].[age]', data)# searches through contacts and returns the age of anyone older than 20

names = [f"{age} " for age in results] #return age
print("Names: " + ",".join(names))

from flask import Flask, jsonify, request
import requests
import json

monsters_url = "https://api.mlsakiit.com/monsters"
resources_url = "https://api.mlsakiit.com/resources"
status_url = "https://api.mlsakiit.com/status"
survivors_url = "https://api.mlsakiit.com/survivors"

app = Flask(__name__)

@app.route('/api/monsters', methods=['GET'])
def get_monsters():
    monsters_response = requests.get(monsters_url)
    if monsters_response.status_code == 200:
        # Save JSON response to a file
        with open("monsters_response.json", "w") as file:
            json.dump(monsters_response.json(), file, indent=4)
        return jsonify(monsters_response.json())
    else:
        return jsonify({"error": "Failed to fetch monsters"}), 500
 
@app.route('/api/resources', methods=['GET'])
def get_resources():
    resources_response = requests.get(resources_url)
    if resources_response.status_code == 200:
        # Save JSON response to a file
        with open("resources_response.json", "w") as file:
            json.dump(resources_response.json(), file, indent=4)
        return jsonify(resources_response.json())
    else:
        return jsonify({"error": "Failed to fetch resources"}), 500
    
@app.route('/api/status', methods=['GET'])
def get_status():
    status_response = requests.get(status_url)
    if status_response.status_code == 200:
        # Save JSON response to a file
        with open("status_response.json", "w") as file:
            json.dump(status_response.json(), file, indent=4)
        return jsonify(status_response.json())
    else:
        return jsonify({"error": "Failed to fetch status"}), 500
 

@app.route('/api/survivors', methods=['GET'])
def get_survivors():
    survivors_response = requests.get(survivors_url)
    if survivors_response.status_code == 200:
        # Save JSON response to a file
        with open("survivors_response.json", "w") as file:
            json.dump(survivors_response.json(), file, indent=4)
        return jsonify(survivors_response.json())
    else:
        return jsonify({"error": "Failed to fetch survivors"}), 500



@app.before_request
def before_request():
    #  Logging all incoming requests
    print(f"Request to: {request.url} with method {request.method}")

@app.after_request
def after_request(response):
    # Logging the response status code
    print(f"Response Status: {response.status}")
    return response

if __name__ == '__main__':
    app.run(debug=True)

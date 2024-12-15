import os
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from flask import Flask, jsonify, request, send_file
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

# Route to survivor's map
@app.route('/generate_map', methods=['GET'])
def generate_map():

    if not os.path.exists('static'):
        os.makedirs('static')  # Create the 'static' folder if it doesn't exist

    # MLSA API to fetch survivor data
    api_url = "https://api.mlsakiit.com/survivors" 
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch data: {str(e)}"}), 500

    # latitude & Longitude
    mean_lat = data['lat'].mean()
    mean_lon = data['lon'].mean()

    # Initialize map
    survivors_map = folium.Map(
        location=[mean_lat, mean_lon], 
        zoom_start=12,
        control_scale=True
    )

    folium.TileLayer(
    tiles='http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png',
    attr='Stamen Toner',
    name='Post-apocalyptic Toner',
    control=True
).add_to(survivors_map)

    # Add markers to the map
    marker_cluster = MarkerCluster().add_to(survivors_map)
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"Survivor ID: {row['survivor_id']}<br>District: {row['district']}",
            icon=folium.Icon(color="blue")
        ).add_to(marker_cluster)

    # Save the map to a temporary file
    html_file_path = "static/survivors_map.html"
    survivors_map.save(html_file_path)

    # Return the file as an API response
    return send_file(html_file_path)

@app.route('/', methods=['GET'])
def home():
    return '''
        <h1>Welcome to the Flask App</h1>
        <p>Available routes:</p>
        <ul>
            <li><a href="/api/monsters">/api/monsters</a> - Get monster data</li>
            <li><a href="/api/resources">/api/resources</a> - Get resource data</li>
            <li><a href="/api/status">/api/status</a> - Get status data</li>
            <li><a href="/api/survivors">/api/survivors</a> - Get survivor data</li>
            <li><a href="/generate_map">/generate_map</a> - Generate survivor map</li>
        </ul>
    '''


# Check server health
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Server is running"}), 200

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

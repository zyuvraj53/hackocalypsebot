import requests
import json

monsters_url = "https://api.mlsakiit.com/monsters"
resources_url = "https://api.mlsakiit.com/resources"
status_url = "https://api.mlsakiit.com/status"
survivors_url = "https://api.mlsakiit.com/survivors"

#monsters_response = requests.get(monsters_url)
#resources_response = requests.get(resources_url)
#status_response = requests.get(status_url)
survivors_response = requests.get(survivors_url)

#### Monsters

#if monsters_response.status_code == 200:
    ## Convert response to JSON
    #data = monsters_response.json()

    ## Save JSON response to a file
    #with open("monsters_response.json", "w") as file:
        #json.dump(data, file, indent=4)  # Pretty formatting with indent
    #print("Response saved to 'monsters_response.json'")
#else:
    #print("Request failed with status code:", monsters_response.status_code)
    

##### Resources
    
#if resources_response.status_code == 200:
    ## Convert response to JSON
    #data = resources_response.json()

    ## Save JSON response to a file
i   #with open("resources_response.json", "w") as file:
        #json.dump(data, file, indent=4)  # Pretty formatting with indent
    #print("Response saved to 'resources_response.json'")
#else:
    #print("Request failed with status code:", response.status_code)
    
#### Status
#if status_response.status_code == 200:
    ## Convert response to JSON
    #data = status_response.json()

    ## Save JSON response to a file
    #with open("status_response.json", "w") as file:
        #json.dump(data, file, indent=4)  # Pretty formatting with indent
    #print("Response saved to 'status_response.json'")
#else:
    #print("Request failed with status code:", status_response.status_code)
    
#### Survivors
if survivors_response.status_code == 200:
    # Convert response to JSON
    data = survivors_response.json()

    # Save JSON response to a file
    with open("survivors_response.json", "w") as file:
        json.dump(data, file, indent=4)  # Pretty formatting with indent
    print("Response saved to 'survivors_response.json'")
else:
    print("Request failed with status code:", survivors_response.status_code)
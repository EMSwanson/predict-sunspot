API = 'https://www.quandl.com/api/v3/datasets/SIDC/SUNSPOTS_D.json?api_key=iMm6-pAoxxUuod3xYxFA'
API_KEY = 'iMm6-pAoxxUuod3xYxFA'

import requests
import json

headers = {
    'API-Key': '',
    'Content-Type': 'application/json'
}

response = requests.get(API)
print(response)
content = response.content
json.dumps(json.loads(content))

with open('sunspots.json', 'w') as write_file:
    json.dump(json.loads(content), write_file)

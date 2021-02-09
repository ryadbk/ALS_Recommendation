import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

NUMBER_RESTAURENT = 2500

url = 'https://api.yelp.com/v3/businesses/search'
api_key = os.getenv('API_KEY')
headers = {'Authorization': 'Bearer %s' % api_key}

originalData = {'businesses': []}

for i in range(0, NUMBER_RESTAURENT, 50):
    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {'term': 'food', 'location': 'Paris', 'limit': '50', 'offset': f'{i}'}
    req = requests.get(url, params=params, headers=headers)
    # print('The status code is {}'.format(req.status_code))
    if req.status_code == 200:
        data = json.loads(req.text)
        for bussiness in data['businesses']:
            originalData['businesses'].append(bussiness)
        print(f"{i} restaurent : Done")
    else:
        break

print(len(originalData['businesses']))
with open("Dataset/bussiness_dataset.json", 'w') as f:
    json.dump(originalData, f, indent=2)

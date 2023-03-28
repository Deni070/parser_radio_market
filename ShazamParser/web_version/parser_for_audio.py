import requests, json
import os
import time
import requests


# File must be in the same directory 
def postRequest(filename):
    data = {
    'api_token': 'fb4199ae3b46a9eca2609ae31e157068',
    'return': 'apple_music,spotify',
    }
    
    # path = os.path.join(os.getcwd() , filename)
    # # print("path: " + os.getcwd())
    files = {
        'file': open(filename, 'rb'),
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    data = json.loads(result.text)
    return data["result"]["artist"], data["result"]["title"]
    # return data

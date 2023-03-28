# import requests
# name = input('Text: ')
# data = {
#     'api_token': 'fb4199ae3b46a9eca2609ae31e157068',
#     'url': f'https://audd.tech/{name}',
#     'return': 'apple_music,spotify',
# }
# result = requests.post('https://api.audd.io/', data=data)
# print(result.text)

import requests
data = {
    'url': 'https://audd.tech/example.mp3',
    'return': 'apple_music,spotify',
    'api_token': 'fb4199ae3b46a9eca2609ae31e157068'
}
result = requests.post('https://api.audd.io/', data=data)
print(result.text)
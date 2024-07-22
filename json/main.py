# import json
# data={
#     'name':'ram',
#     'age':20
# }
# print(data)
# # distionary to json
# data = json.dumps(data)
# print(data)
# # json to dictionary
# data = json.loads(data)
# print(data)
import requests
url ="https://jsonplaceholder.typicode.com/users"
response = requests.get(url).json()
for i in response:
    print(i['name'])
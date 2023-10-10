# import requests
# URL = "http://127.0.0.1:8000/student_info/2"
# r = requests.get(url = URL)
# data = r.json()
# print ( type( data))
# print ( data)



import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Sonam',
    'roll': 101,
    'city': 'Ranchi'
}

json_data = json.dumps (data)
r = requests.post (url = URL, data = json_data)
data = r.json()
print (data)
# =================================================== Serialize ===================================================
# import requests
# URL = "http://127.0.0.1:8000/student_info/2"
# r = requests.get(url = URL)
# data = r.json()
# print ( type( data))
# print ( data)


# =================================================== Deserialize ===================================================
# import requests
# import json
# URL = "http://127.0.0.1:8000/stucreate/"

# data = {
#     'name': 'Sonam',
#     'roll': 101,
#     'city': 'Ranchi'
# }

# json_data = json.dumps (data)
# r = requests.post (url = URL, data = json_data)
# data = r.json()
# print (data)

# =================================================== CRUD Operations =========================================================
# =============== Read Operations =================
import requests
import json
URL = "http://127.0.0.1:8000/stuapi/"
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print (data)

# get_data(2)


# =============== Create Operations =================
def post_data():
    data = {
    'name': 'Ravi',
    'roll': 104,
    'city': 'Dhanbad'
    }
    json_data = json. dumps (data)
    r = requests.post (url = URL, data = json_data)
    data = r.json()
    print (data)
# post_data ()


# =============== Update Operations =================

def update_data() :
    data = {
    'id': 3,
    'name': 'Rohit',
    'city': 'Ranchi'
    }
    json_data = json.dumps (data)
    r = requests.put (url = URL, data = json_data)
    data = r.json()
    print (data)
# update_data()


def delete_data():
    data = { 'id': 5}
    json_data = json.dumps (data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print (data)
# delete_data()



# =============================================================================================================================

# =================================================== CRUD Operations with validation =========================================================
# =============== Read Operations =================
import requests
import json
URL = "http://127.0.0.1:8000/stuapi2/"
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print (data)

# get_data(2)


# =============== Create Operations =================
def post_data():
    data = {
    'name': 'Ravi',
    'roll': 105,
    'city': 'Dhanbad'
    }
    json_data = json. dumps (data)
    r = requests.post (url = URL, data = json_data)
    data = r.json()
    print (data)
# post_data ()


# =============== Update Operations =================

def update_data() :
    data = {
    'id': 5,
    'name': 'Rohit',
    'city': 'Ranchi'
    }
    json_data = json.dumps (data)
    r = requests.put (url = URL, data = json_data)
    data = r.json()
    print (data)
# update_data()


def delete_data():
    data = { 'id': 5}
    json_data = json.dumps (data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print (data)
# delete_data()
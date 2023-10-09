import requests
URL = "http://127.0.0.1:8000/student_info/2"
r = requests.get(url = URL)
data = r.json()
print ( type( data))
print ( data)
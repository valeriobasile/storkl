import requests

r = requests.get('http://127.0.0.1:5000/u/valerio')
res = r.json()
print res

r = requests.post('http://127.0.0.1:5000/u/new', data={'username' : 'valerio', 'email' : 'valerio@storkl.net'})
res = r.json()
print res

r = requests.get('http://127.0.0.1:5000/u/valerio')
res = r.json()
print res


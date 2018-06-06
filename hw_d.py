import requests

r = requests.get("https://swapi.co/api/people")
d = r.json()

for c in d['results']:
	print(c["name"])
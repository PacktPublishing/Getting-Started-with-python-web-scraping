
import urllib.request, urllib.parse, json
location = {"lon":49, "lat":-123}
query = urllib.parse.urlencode(location)
resp = urllib.request.urlopen("http://api.open-notify.org/iss-now.json?" + query)
obj = json.loads(resp.read().decode("utf8"))
print(obj)


import requests
location = {"lon":49, "lat":-123}
resp = requests.get("http://api.open-notify.org/iss-now.json", params=location)
obj = resp.json()
print(obj)


import requests
parameters = {"lon":-79, "lat":45, "api_key": "<YOUR_API_KEY>"}
resp = requests.get("https://api.nasa.gov/planetary/earth/imagery", params=parameters)
obj = resp.json()
print(obj)


import urllib.request, urllib.parse, json
parameters = {"lon":-79, "lat":45, "api_key": "<YOUR_API_KEY>"}
query = urllib.parse.urlencode(parameters)
resp = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery?" + query)
obj = json.loads(resp.read().decode("utf8"))
print(obj)




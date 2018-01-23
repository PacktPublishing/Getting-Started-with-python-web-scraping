
# good example using requests
import requests 
url = "https://www.google.com/"
header = {
    "From":"Your Name <Your Email>"
}

response = requests.get(url, headers=header)
if response.status_code == 200:
    html = response.text 
    print(html)
else:
    print("Error", response.status_code, response.reason)

# basic example using urllib 
import urllib.request
url = "https://www.google.com/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()
print(html)
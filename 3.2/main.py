import requests
resp = requests.get("https://api.ip2country.info/ip?184.68.182.250")
obj = resp.json()
print(obj.get("countryName")) # Canada
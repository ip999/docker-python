# import required libraries
import requests
import json

# set URL for ifconfig.co API
url = "https://ifconfig.co/json"

# use requests to fetch the URL
content = requests.get(url)

# parse the JSON response
parsed = json.loads(content.text)

# print out entire JSON response
print("JSON Body:")
print(json.dumps(parsed, indent=4, sort_keys=True))

# print out just the IP address
print("IP: " + parsed["ip"])

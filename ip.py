# import required libraries
import requests
import json

# set URL for ifconfig.co API
url = "https://ifconfig.co/json"

# use requests to fetch the URL
content = requests.get(url)

# print out entire JSON response
print("JSON Body:\n" + content.text)

# parse the JSON response
process_content = json.loads(content.text)

#print out the IP address
print("IP: " + process_content["ip"])

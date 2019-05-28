import requests
import json
url = "https://ifconfig.co/json"
content = requests.get(url)

# print out entire JSON response
print("JSON Body:\n" + content.text)

#print out just the IP address
process_content = json.loads(content.text)
print("IP: " + process_content["ip"])

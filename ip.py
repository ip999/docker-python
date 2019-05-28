import requests
url = "https://ifconfig.co/json"
content = requests.get(url)
print(content.text)

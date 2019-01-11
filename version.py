import requests

r = requests.get("https://raw.githubusercontent.com/tlaz4/lab1/master/version.py")
print(r.text)

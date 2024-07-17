import requests

response = requests.get("https://wizard-world-api.herokuapp.com/Houses")

print(response.ok)
print(response.status_code)
print(response.json())

if response.ok:
    print("The request is ok")
    
import requests

response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error: API request failed")

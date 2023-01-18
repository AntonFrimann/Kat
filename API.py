import requests

def getData():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')

    if response.status_code == 200:
        data = response.json()
        return data

    else:
        print("Error: API request failed")
        return []

def getUrls():
    data = getData()
    urls = []
    for cat in data:
        urls.append(cat['url'])
    return urls

if __name__ == "__main__":
    print(getData())

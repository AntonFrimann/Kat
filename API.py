import requests, random

urlList = []

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

def getUrl():
    global urlList
    if len(urlList) < 1:
        urlList = getUrls()
    url = urlList.pop(random.randint(0, len(urlList)))
    return url

if __name__ == "__main__":
    print(getData())

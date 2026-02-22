import requests

url = "https://libretranslate.de/translate"

data = {
    "q":"Hello how are you",
    "source":"en",
    "target":"hi",
    "format":"text"
}

response = requests.post(url,data=data)
result = response.json()
print(result)
#print("translated text:",result["translatedText"])
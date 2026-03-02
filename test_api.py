import requests

url = "http://localhost:5001/translate"

data = {
    "q":"what happened",
    "source":"en",
    "target":"hi",
    "format":"text"
}

response = requests.post(url,data=data)
result = response.json()
print(result)
#print("translated text:",result["translatedText"])
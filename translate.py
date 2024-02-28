import requests

soz = input("so'zni kiriting")
detect_url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
payload = {"q": soz}

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "73f34bdfe1msh69736d5739eaf4cp1c8e73jsn6becb8c79d13",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}
response = requests.post(detect_url, data=payload, headers=headers)
language = response.json()["data"]["detections"][0][0]["language"]
translate_url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

if language == "en":
    payload = {
        "q": soz,
        "target": "uz",
        "source": "en"
    }
    response = requests.post(translate_url, data=payload, headers=headers)
    print(response.json()["data"]["translations"][0]["translatedText"])
elif language == "uz":
    payload = {
        "q": soz,
        "target": "en",
        "source": "uz"
    }
    response = requests.post(translate_url, data=payload, headers=headers)
    print(response.json()["data"]["translations"][0]["translatedText"])

else:
    print("soz xato kiritildi")

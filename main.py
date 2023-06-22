import requests
ttext=input("metin girin : ")
translate_url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
translate_payload = {
	"q": ttext,
	"target": "en",
	"source": "tr"
}
translate_headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "6f49bac845msh584b8be3d0b6c24p1b29d0jsndac34818b55e",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

translate_response = requests.post(translate_url, data=translate_payload, headers=translate_headers)
translated_text = translate_response.json()['data']['translations'][0]['translatedText']

sentiment_url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"
sentiment_payload = [
	{
		"id": "1",
		"language": "en",
		"text": translated_text
	}
]
sentiment_headers = {
	"content-type": "application/json",
	"Accept": "application/json",
	"X-RapidAPI-Key": "6f49bac845msh584b8be3d0b6c24p1b29d0jsndac34818b55e",
	"X-RapidAPI-Host": "sentiment-analysis9.p.rapidapi.com"
}

sentiment_response = requests.post(sentiment_url, json=sentiment_payload, headers=sentiment_headers)
print(translated_text)
print(sentiment_response.json())

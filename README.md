# Using Google Translate and Sentiment Analysis APIs

This Python script uses Google Translate and Sentiment Analysis APIs to translate and analyze sentiment of texts. The input text is in Turkish, and after the translation, sentiment analysis is performed on the English version.

## How It Works?

1. **The script asks for a text input in Turkish from the user.**

2. **The input text is sent to Google Translate API via an HTTP POST request.** This API service translates the text into English. The required API keys and other details are specified in `translate_headers` and `translate_payload`.

3. **After the translation process, the translated English text is sent to the Sentiment Analysis API.** This API analyzes the emotional tone of the text and provides a sentiment score.


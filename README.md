# GoogleGeminiAI
In this project I use Python to send a text prompt to Google Gemini AI and get a response

First we need to obtain our Gemini AI API key by going onto Google's AI Developer portable you can create a free one.
![Screenshot](https://github.com/jasnnh/GoogleGeminiAI/blob/main/1.jpg)

Edit GeminiAI.py and replace API = "" with our API key
Now run cmd and type python main.py and enter your prompt
![Screenshot](https://github.com/jasnnh/GoogleGeminiAI/blob/main/2.jpg)

to break it down in the GeminiAI.py we are using the Python request library to make an HTTP POST request to:
https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent
this is the AI model we are using and providing the API key with our prompt message
the prompt message is formatted into a json format first for gemini to read it and give a response and
gemini respond in json format as well.

if the API is incorrect then the request will be refused/error.

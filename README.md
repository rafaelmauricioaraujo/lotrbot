**LOTRBOT**

The RPG Chatbot game based on adventure world of Lord of The Ring

_Powered by Rasa_

to start server

```python
rasa run --enable-api -m models --cors "*" --debug
```

parse messages to retrieve intents and entities
```python
url: http://localhost:5005/model/parse
HTTP: POST

{
"text": message
}
```

retrieve response to core rasa

```python
url: http://localhost:5005/webhooks/rest/webhook
HTTP: POST

{
	"sender": "123",
	"message": message (string)
}

```

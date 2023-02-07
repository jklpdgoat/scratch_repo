import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/tools")
todos = json.loads(response.text)

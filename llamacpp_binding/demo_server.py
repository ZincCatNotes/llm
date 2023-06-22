import requests

url = "http://localhost:8000/v1/chat/completions"
headers = {"accept": "application/json", "Content-Type": "application/json"}

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write me quicksort in Python."},
    ],
    "max_tokens": 200,
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])

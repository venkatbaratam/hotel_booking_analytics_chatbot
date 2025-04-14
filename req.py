import requests

url = "http://127.0.0.1:5000/chat"
data = {"question": "What is the overall cancellation rate?"}

headers = {
    "Authorization": "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"  # Replace with your actual API key
}

response = requests.post(url, json=data, headers=headers)
print(response.json())

# credit to https://www.youtube.com/watch?v=n28awivN2FA

import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3" 
token = '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'

prompt = input("Prompt: ")

headers = {
'Authorization': f'Bearer {token}'
}

def query (payload):
    response = requests.post(url, headers=headers, json=payload) 
    return response.json()

output = query({
"inputs": prompt,
})

text = str(output).strip("'{[}]")
pop = len("generated_text': '") + len(prompt) + 1
text = text[pop:]

print(text.replace('\n', ' '))
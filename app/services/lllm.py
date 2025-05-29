import requests, json
from app.core.config import settings



MODEL = 'llama3.2' 
system_prompt = (
    """
Extract the email summary and respond only with a json object in this format:
{
    "date": "Date of the email in YYYY-MM-DD format",
    "from": "Sender's email address",
    "subject": "Email subject",
    "description": "Brief description of the email content",
    "key takeaways": "actions from the email, important information, or any other relevant details"
}
"""
)


def gen_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False 
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        # print(result.get("response", ""))
        return result.get("response", "")
    else:
        raise Exception(f"Failed to get response: {response.status_code}, {response.text}")

def gen_ollama_stream(prompt):
    url = "http://localhost:11434/api/generate" 
    payload = {
        "model": MODEL,
        "prompt": system_prompt + prompt,
        "stream": True
    }

    with requests.post(url, json=payload, stream=True) as response:
        full_reply = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if not data.get("done", False):
                    chunk = data["response"]
                    print(chunk, end="", flush=True)  # live output
                    full_reply += chunk
        # print("\n\nFinal response:\n", full_reply)
        return full_reply.strip()







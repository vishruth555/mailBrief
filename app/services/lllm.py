import requests, json

MODEL = 'gemma3:latest'
system_prompt = (
    "You must respond ONLY with a valid JSON array of objects. "
    "Each object must contain the fields: 'sender', 'purpose', and 'content'. "
    "Do NOT include any extra text before or after the JSON array. Example:\n"
    "[\n"
    "  {\"sender\": \"Alice\", \"purpose\": \"Greeting\", \"content\": \"Hello!\"},\n"
    "  {\"sender\": \"Bob\", \"purpose\": \"Reply\", \"content\": \"Hi there!\"}\n"
    "]"
)


def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": MODEL,
        "prompt": system_prompt + prompt,
        "stream": False 
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        print(result)
        return result.get("response", "")
    else:
        raise Exception(f"Failed to get response: {response.status_code}, {response.text}")

def query_ollama_stream(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": MODEL,
        "prompt": prompt,
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



# Example usage
if __name__ == "__main__":
    prompt = "hi there"
    query_ollama_stream(prompt)
    print()
    # reply = query_ollama(prompt)
    # print("Ollama says:\n", reply)

import requests, json
from app.core.config import settings
import os




MODEL = 'llama3.2:1b'
# MODEL = 'gemma3:4b' 


if os.getenv("RUNNING_IN_DOCKER") == "true":
    URL = "http://host.docker.internal:11434/api/generate"
else:
    URL = "http://localhost:11434/api/generate"



system_prompt = (
    "\n\n"  
    "--- END OF EMAIL --- BEGIN INSTRUCTIONS ---\n\n"
    "TASK: Read the email written above carefully.\n"
    "You need to find 5 pieces of information from this email.\n\n"
    "INFORMATION TO EXTRACT:\n"
    "1.  **Email Date**: Find the date the email was sent. Write this date in YYYY-MM-DD format (for example: 2023-01-15).\n"
    "2.  **Sender Email**: Find the email address of the person who sent the email.\n"
    "3.  **Email Subject**: Find the subject line of the email.\n"
    "4.  **Email Description**: Write a very short summary of what the email is about. One or two sentences is best.\n"
    "5.  **Key Takeaways**: List any important things from the email, like actions to do, important news, or questions asked.\n\n"
    "OUTPUT FORMAT INSTRUCTIONS:\n"
    "You MUST give your answer as a JSON object. \n"
    "Do NOT write any other words or sentences before or after the JSON object. Only the JSON.\n"
    "Your JSON output MUST look EXACTLY like this example structure, with your extracted information replacing the placeholders:\n\n"
    "{\n"
    "  \"date\": \"(PUT THE EXTRACTED YYYY-MM-DD DATE HERE)\",\n"
    "  \"from\": \"(PUT THE SENDER'S EMAIL ADDRESS HERE)\",\n"
    "  \"subject\": \"(PUT THE EMAIL SUBJECT HERE)\",\n"
    "  \"description\": \"(PUT YOUR SHORT EMAIL DESCRIPTION HERE)\",\n"
    "  \"key takeaways\": \"(PUT THE KEY TAKEAWAYS HERE)\"\n"
    "}\n\n"
    "Make sure your final output is a valid JSON object. Fill in the information carefully. AND DO NOT INCLUDE LINKS.\n"
)

def generate_payload(prompt,isStream: bool):
    payload = {
        "model": MODEL,
        "prompt": system_prompt + prompt,
        "stream": isStream,
        "options": {
            "num_ctx": 	8192,
            # "num_ctx": 	32768,
            "temperature": 0.4,
        },
        "format": {
            "type": "object",
            "properties": {
                "date": {
                "type": "string"
                },
                "from": {
                "type": "string"
                },
                "subject": {
                "type": "string"
                },
                "description": {
                "type": "string"
                },
                "key takeaways": {
                "type": "string"
                }
            },
            "required": [
                "date",
                "from",
                "subject",
                "description",
                "key takeaways"
            ]
            }
    }

    return payload

def gen_ollama(prompt):
    payload = generate_payload(prompt, False)

    response = requests.post(URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        # print(result.get("response", ""))
        return result.get("response", "")
    else:
        raise Exception(f"Failed to get response: {response.status_code}, {response.text}")

def gen_ollama_stream(prompt):

    payload = generate_payload(prompt, True)

    with requests.post(URL, json=payload, stream=True) as response:
        full_reply = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if not data.get("done", False):
                    chunk = data["response"]
                    print(chunk, end="", flush=True)  # live output
                    full_reply += chunk
        print("\n\nFinal response:\n", full_reply)
        return full_reply.strip()







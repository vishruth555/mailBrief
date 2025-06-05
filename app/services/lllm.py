import requests, json
from app.core.config import settings
import os




MODEL = 'llama3.2:1b' 
# MODEL = 'gemma3:1b'


# if os.getenv("RUNNING_IN_DOCKER") == "true":
#     URL = "http://host.docker.internal:11434/api/generate"
# else:
#     URL = "http://localhost:11434/api/generate"

URL = "http://localhost:11434/api/generate"


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

prompt_text = (
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
    "Make sure your final output is a valid JSON object. Fill in the information carefully."
)

def gen_ollama(prompt):
    url = URL
    payload = {
        "model": MODEL,
        "prompt": prompt + prompt_text,
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
    url = URL
    payload = {
        "model": MODEL,
        "prompt": system_prompt + prompt + prompt_text,
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







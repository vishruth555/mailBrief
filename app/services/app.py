from app.services.imap import get_email_body, estimate_tokens
from app.services.lllm import gen_ollama_stream
from app.services.gemini import gen_gemini
from app.core.config import settings
import json
import re



def extract_json_from_summary(summary):
    # Match JSON-like block
    match = re.search(r'\{.*?\}', summary, re.DOTALL)
    if match:
        json_str = match.group(0)
        try:
            data = json.loads(json_str)
            return data
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
            return None
    else:
        print("No JSON found in summary")
        return None



def query_ollama(number_of_emails, type):

    print("Starting email summarization with Ollama...")
    print("Fetching the latest emails...")
    query = "summarize the following emails: \n\n"
    emails = get_email_body(number_of_emails, type)
    query += emails

    print("Querying Ollama with the following prompt:\n", query)

    print("\n\n\n\nEstimated tokens: ", estimate_tokens(query))
    print("\n\n\n\nSummary of emails:\n")
    # summary = query_ollama(query)
    summary = gen_ollama_stream(query)
    print("-"*100)
    return extract_json_from_summary(summary)

def query_gemini(number_of_emails: int, type: str):

    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the configuration.")
    
    
    print("Starting email summarization with gemini...")
    print("Fetching the latest emails...")
    query = get_email_body(number_of_emails, type)

    print("Querying gemini with the following prompt:\n")

    print("\n\n\n\nEstimated tokens: ", estimate_tokens(query))
    print("\n\n\n\nSummary of emails:\n")
    summary = gen_gemini(query)
    print("-"*100)
    return json.loads(summary)
     
    
    


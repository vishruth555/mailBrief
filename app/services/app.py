from app.services.imap import get_email_body, estimate_tokens
from app.services.lllm import query_ollama_stream, query_ollama
from app.services.gemini import generate
import json



def main():
    print("Starting email summarization...")
    print("Fetching the latest emails...")
    query = "summarize the following emails: \n\n"
    emails = get_email_body(5)
    query += emails

    print("Querying Ollama with the following prompt:\n", query)

    print("\n\n\n\nEstimated tokens: ", estimate_tokens(query))
    print("\n\n\n\nSummary of emails:\n")
    summary = query_ollama(query)
    print("-"*100)
    return summary

def query_gemini(number_of_emails: int, type: str):
    print("Starting email summarization...")
    print("Fetching the latest emails...")
    query = get_email_body(number_of_emails, type)

    print("Querying gemini with the following prompt:\n")

    print("\n\n\n\nEstimated tokens: ", estimate_tokens(query))
    print("\n\n\n\nSummary of emails:\n")
    summary = generate(query)
    print("-"*100)
    return json.loads(summary)
     
    
    

if __name__ == "__main__":
    main()
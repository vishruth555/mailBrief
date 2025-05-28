# app/api/v1/endpoints/example.py
from fastapi import APIRouter
import re, json, time

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@router.get("/summary")
def get_summary():
    from app.services.app import main
    summary = main()
    return summary

@router.post("/gemini")
def get_summary(number_of_emails: int, type: str):
    print(f"Parsing {number_of_emails} emails of type {type}")
    from app.services.app import query_gemini
    summary = query_gemini(number_of_emails, type)
    return summary



@router.post("/parse")
def parse_email(number_of_emails: int, type: str):
    print(f"Parsing {number_of_emails} emails of type {type}")
    text = """{
  "summary": [
    {
      "subject": "Vishruth, thanks for being a valued member",
      "description": "LinkedIn is offering Vishruth a free month of LinkedIn Premium.",
      "key takeaways": "The email highlights benefits like top applicant jobs, LinkedIn Learning, AI Writing Assistant, and profile views, with a call to action to unlock the free trial, which ends on May 9, 2025."
    },
    {
      "subject": "Hi Vishruth Ps Reddy, Event order ID 7832 has been received! - Initium Fest",
      "description": "Initium Fest confirms receipt of order #7832 from Vishruth and informs that the transaction is under process.",
      "key takeaways": "The email states that the e-ticket will be sent within 24 hours and includes order details for a 'STAND UP' ticket, costing ₹200.00. It also includes links to their Instagram and contact information."
    },
    {
      "subject": "Payments made Fast and Super Easy  with YONO Quick Pay",
      "description": "YONO SBI informs that this is a system generated mail, please do not reply to this mail.",
      "key takeaways": "The email contains a link to unsubscribe and a disclaimer about State Bank never requesting confidential information via email."
    }
  ]
}"""
    time.sleep(1)
    return json.loads(text)

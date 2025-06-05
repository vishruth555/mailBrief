# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
from app.core.config import settings
from google import genai
from google.genai import types




def gen_gemini(email_body: str = None):
    client = genai.Client(
        api_key=settings.GEMINI_API_KEY,
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=email_body),
            ],
        ),
    ]

    prompt_text = (
    "\n\n"
    "Please analyze the email content immediately preceding this instruction. "
    "Your task is to summarize this email by extracting specific pieces of information. "
    "Ensure your entire response is a single JSON object with the following keys and corresponding values from the email:\n"
    "- \"date\": The date of the email, formatted as YYYY-MM-DD.\n"
    "- \"from\": The sender's email address.\n"
    "- \"subject\": The subject line of the email.\n"
    "- \"description\": A brief description of the email's main content.\n"
    "- \"key takeaways\": Important actions, decisions, or information mentioned in the email.\n"
    "Adhere strictly to this JSON structure and the field descriptions provided in the system instructions. Do not include any text outside of this JSON object."
    )

    contents.append(prompt_text)


    generate_content_config = types.GenerateContentConfig(
        temperature=0.1,
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            properties = {
                "date": genai.types.Schema(
                    type = genai.types.Type.STRING,
                ),
                "from": genai.types.Schema(
                    type = genai.types.Type.STRING,
                ),
                "subject": genai.types.Schema(
                    type = genai.types.Type.STRING,
                ),
                "description": genai.types.Schema(
                    type = genai.types.Type.STRING,
                ),
                "key takeaways": genai.types.Schema(
                    type = genai.types.Type.STRING,
                ),
            },
        ),
        system_instruction=[
            types.Part.from_text(text="""Extract the email summary and respond only with a json object in this format:
            {
                \"date\": \"Date of the email in YYYY-MM-DD format\",
                \"from\": \"Sender's email address\",
                \"subject\": \"Email subject\",
                \"description\": \"Brief description of the email content\",
                \"key takeaways\": \"actions from the email, important information, or any other relevant details\"
            }"""),
                    ],
    )

    response = ''

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        response += chunk.text

    return response


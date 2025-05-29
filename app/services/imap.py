

import imaplib
import email
from email.header import decode_header
from app.core.config import settings


username = settings.EMAIL_USERNAME
password = settings.EMAIL_PASSWORD
imap_server = settings.IMAP_SERVER



def get_email_body(NumberOfEmails: int, type: str ):
    text = ''
    # Connect to the server
    mail = imaplib.IMAP4_SSL(imap_server)

    # Login to your account
    mail.login(username, password)

    # Select the mailbox
    mail.select("inbox")

    # Search for unread emails only
    queryAll = 'ALL'
    queryUnread = 'UNSEEN'
    status, messages = mail.search(None, type)

    # Convert to list of email IDs
    mail_ids = messages[0].split()

    # Get only the last 10 unread emails

    mail_ids = mail_ids[-NumberOfEmails:]

    for i in mail_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(i, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")

                print("Subject:", subject)
                print("From:", msg.get("From"))
                print("Date:", msg.get("Date"))

                text += subject + "\n" + msg.get("From") + "\n" + msg.get("Date")

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            continue
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print("Body:", body)
                            text += "\n" + body
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                    # print("Body:", body)
                    text += "\n" + body
        print("-" * 50)
        # Logout
    mail.logout()
    return text

def estimate_tokens(text):
    return len(text) // 2  # Rough estimate






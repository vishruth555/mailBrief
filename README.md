# 📬 Email Summarizer Dashboard

A responsive dashboard for summarizing your recent emails using Gemini 2.0 Flash. You can choose how many emails to fetch (1–10) and filter between all or only unseen emails.

![Screenshot 1](assets/1.png)
![Screenshot 2](assets/2.png)

---

## Features

* Choose number of emails (1–10)
* Select between **all** or **unseen** types
* Responsive dark-themed UI

---

## Requirements

* Python 3.9+
* pip
* Access to:

  * A valid email account (Gmail, Outlook, etc.)
  * [Google Gemini API key](https://aistudio.google.com/app/apikey)

---

## Environment Variables

Create a `.env` file in the **root directory** with the following contents:

```env
EMAIL_USERNAME = '<your_email@example.com>'
EMAIL_PASSWORD = '<your_email_app_password>'
IMAP_SERVER = '<imap.gmail.com>'
GEMINI_API_KEY = '<your_google_gemini_api_key>'
```

> ℹ️ The email password should be an **App Password**, which you can generate in your email provider’s security settings (e.g., [Google App Passwords](https://myaccount.google.com/apppasswords)).

> 🧠 The Gemini API key is **free** and can be generated from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/email-summarizer.git
   cd email-summarizer
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your credentials to `.env` as shown above.**

4. **Run the server:**

   ```bash
   python run.py
   ```

5. **Access the dashboard at:**

   ```
   http://127.0.0.1:8000/
   ```

---

## Notes

* Currently uses **Gemini 2.0 Flash** via API.
* **Ollama** does not support **structured JSON outputs** yet.
* Once available, the summarization process will be migrated to run fully locally.

---

## License

MIT License

---

## Contributing

Pull requests and issues are welcome.

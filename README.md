# 📬 Email Summarizer Dashboard

A responsive dashboard for summarizing your recent emails using either Gemini 2.0 Flash or Ollama. You can choose the number of emails to fetch and have them summarized one by one.

## Important Considerations

- The **free** Gemini API key offers **faster** summarization but at the cost of your privacy.
- Ollama models enable a fully local experience, although processing speeds depend on your hardware.

![Screenshot 1](assets/1.png) 
![Screenshot 2](assets/2.png)


---



## Prerequisites

Create a `.env` file in the **root directory** with the following contents:

```env
EMAIL_USERNAME = '<your_email@example.com>'
EMAIL_PASSWORD = '<your_email_app_password>'
IMAP_SERVER = '<imap.gmail.com>'
GEMINI_API_KEY = '<your_google_gemini_api_key>'
```

ℹ️ The email password should be an **App Password**, which you can generate in your email provider’s security settings (e.g., [Google App Passwords](https://myaccount.google.com/apppasswords)).

🧠 The Gemini API key is **free** and can be generated from [Google AI Studio](https://aistudio.google.com/app/apikey). It is **not** mandatory!


---

## Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/vishruth555/mailBrief.git
   cd mailBrief
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
   http://127.0.0.1:5000/
   ```

---

## 🚀 Running with Docker

### 

1. **Clone this repository:**

   ```bash
   git clone https://github.com/vishruth555/mailBrief.git
   cd mailBrief
   ```

2. **📦 Build the run Docker Image**

   ```bash
   docker build -t mailbrief .
   docker run --network=host -d mailbrief
   ```



## Notes

- Uses **Gemini 2.0 Flash** via API for rapid summarization.
- **Ollama** models may require more processing time for large emails and might be less optimal on systems with smaller GPUs. However, as all data processing is performed locally, this option is recommended when working with sensitive data (e.g., company mail accounts).
- Change ollama model to your liking in app/services/lllm.py, it is currently using gemma3:1b
---

## License

MIT License

---

## Contributing

Pull requests and issues are welcome.
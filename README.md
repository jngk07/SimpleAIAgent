# Email Agent Demo with smolagents

This is a demo project showing how to build an AI-powered Email Agent that:
- Reads emails from Gmail
- Checks calendar availability
- Sends notifications via WhatsApp

---

## Setup Instructions

 
1. **Create a Python virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install requirements**
```bash
pip install -r requirements.txt
```

4. **Configure Gmail & Calendar API**
- Enable Gmail + Calendar API in Google Cloud Console
- Download credentials.json to the root of this project
- On first run, it will create `token.json` after OAuth flow

5. **Configure Twilio WhatsApp**
- Sign up at https://twilio.com/whatsapp
- Get sandbox credentials and phone number
- Replace your details in `whatsapp_tool.py`

6. **Run the agent**
```bash
python main.py
```

It will check for new emails and run the Email Agent pipeline.

---

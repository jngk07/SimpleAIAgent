from gmail_reader import get_unread_emails
from calendar_tool import check_availability
from whatsapp_tool import send_whatsapp_alert

# Dummy agent logic
emails = get_unread_emails()

for email in emails:
    subject = email.get("subject")
    body = email.get("snippet")
    print(f"Processing Email: {subject}")

    if "meeting" in body.lower():
        available = check_availability()
        print(f"Calendar Available? {available}")
        if available:
            send_whatsapp_alert(subject, "Meeting requested. You are available.")

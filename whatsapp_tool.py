from twilio.rest import Client

# Replace with your actual Twilio details
account_sid = "Your Twillo SID"
auth_token = "YourTwilloToken"
from_number = "whatsapp:+14155238886"
to_number = "whatsapp:+16127026856"

def send_whatsapp_alert(subject, message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        from_=from_number,
        body=f"Email Alert:\nSubject: {subject}\n{message}",
        to=to_number
    )

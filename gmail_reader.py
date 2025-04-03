from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_unread_emails():
    creds = Credentials.from_authorized_user_file("token.json")
    service = build("gmail", "v1", credentials=creds)
    results = service.users().messages().list(userId="me", labelIds=["INBOX"], q="is:unread").execute()
    messages = results.get("messages", [])
    emails = []
    for msg in messages:
        m = service.users().messages().get(userId="me", id=msg["id"]).execute()
        emails.append({
            "subject": next((h["value"] for h in m["payload"]["headers"] if h["name"] == "Subject"), ""),
            "snippet": m.get("snippet", "")
        })
    return emails
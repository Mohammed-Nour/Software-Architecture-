import smtplib
from email.message import EmailMessage
import json

# SMTP server settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "yehiasobeh@gmail.com"  # Replace with your email
EMAIL_PASSWORD = ""  # Replace with your email app password


def apply_publishing(message):
    """
        Sends an email with the given message.
        """
    try:
        print(f"Connecting to SMTP server {SMTP_SERVER} on port {SMTP_PORT}...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email = EmailMessage()
            email["From"] = EMAIL_ADDRESS
            email["To"] = ["yehiasobeh2@gmail.com"]  # Replace with your recipient(s)
            email["Subject"] = "New Message from Publish Service"
            email.set_content(message)

            server.send_message(email)
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

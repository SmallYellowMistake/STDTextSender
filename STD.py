from twilio.rest import Client

# Twilio account credentials
account_sid = 'your personal Accound_SID'
auth_token = 'your auth token'
client = Client(account_sid, auth_token)

def send_anonymous_sms(to_number, message):
    from_number = "your number"
    try:
        client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"Message sent to {to_number}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Example usage
to_number = input("Enter the recipient's phone number: ")
message = "This is an anonymous notification regarding your health. You might want to get tested for STDs."
send_anonymous_sms(to_number, message)

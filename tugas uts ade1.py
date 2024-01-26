aplikasi mengirimkan pesan Whatsapp terenkripsi dengan kriptografi Caesar dan encoding Base 64 dalam bahasa PHP atau bahasa Python.  Upload di Github anda, dan share urlnya sebagai jawaban and
from twilio.rest import Client
import base64

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'  # Format: +1234567890

# Target WhatsApp number
whatsapp_to = 'whatsapp:+1234567890'

# Message content
message_text = 'Hello, this is a Base64 encoded message.'

# Encode message using Base64
encoded_message = base64.b64encode(message_text.encode()).decode()

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send WhatsApp message
message = client.messages.create(
                              body=encoded_message,
                              from_=twilio_phone_number,
                              to=whatsapp_to
                          )

print(f"Message sent successfully. SID: {message.sid}")

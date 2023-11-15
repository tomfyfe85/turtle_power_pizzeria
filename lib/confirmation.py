from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()


token = os.getenv("AuthToken")
sid = os.getenv("AuthSid")
test_number = os.getenv("TestNumber")
twilio_number = os.getenv("TwilioNumber")


account_sid = sid
auth_token = token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=twilio_number,
  body='test 6',
  to=test_number
)

print(message.sid)

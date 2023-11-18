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


class Confirmation:
    def __init__(self, number):
        self._number = number

    def confirm_message(self):
        message = client.messages.create(
            from_=twilio_number, body="Thank you for your order!", to=self._number
        )
        return message.sid

from lib.confirmation import Confirmation
import os
from dotenv import load_dotenv

load_dotenv()
test_number = os.getenv("TestNumber")
twilio_number = os.getenv("TwilioNumber")


"""
#confirm_order should send a SMS to the given number using twilio
"""


def test_a_confirmation_SMS_is_sent():
    confirm = Confirmation(test_number)
    assert confirm.confirm_message() is not None

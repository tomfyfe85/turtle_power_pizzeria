from lib.confirmation import Confirmation
import os
from dotenv import load_dotenv
from unittest import mock

load_dotenv()
test_number = os.getenv("TestNumber")
twilio_number = os.getenv("TwilioNumber")
Auth_Sid = os.getenv("AuthSid")

"""
#confirm_order should send a SMS to the given number using twilio
"""


@mock.patch("lib.confirmation.client.messages.create")
def test_a_confirmation_SMS_is_sent(create_message_mock):
    confirm = Confirmation(test_number)

    message = "Test message"
    expected_sid = Auth_Sid
    create_message_mock.return_value.sid = expected_sid

    to = test_number
    from_ = twilio_number
    sid = confirm.confirm_message()

    assert create_message_mock.called is True
    assert sid == expected_sid

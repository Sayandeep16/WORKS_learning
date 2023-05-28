# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC10a2716899449decdfdcec90687c3081"
auth_token = "7047eadc5a4b188229cccf8f9505455b"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="bichi",
  from_="+12705144781",
  to="+917872639252"
)
print(message.sid)
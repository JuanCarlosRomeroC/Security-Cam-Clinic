# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC62188133685cdf2b007c60b4ecd7d67a'
auth_token = '0c36936b0bf1b6d794ac0a9163d752eb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18564463809',
                     to='+918921891745'
                 )

print(message.sid)
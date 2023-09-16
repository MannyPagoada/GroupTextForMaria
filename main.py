#Importing twilio
from twilio.rest import Client

#set up your Twilio credentials
account_sid = 'AC5ec67abf27443c0f176edb42b57edbca'
auth_token = '8ec6323ad508b465e498b6f876751f66'

#initialize the twilio client
client = Client(account_sid, auth_token)


#list of group pf numbers 
group_numbers=[
    '+14088578761',
    '+13232828574',
]

#message to send
message_to_send="This is a test for the catholic club text message system."


def sendGroupMessage(group_numbers, message):
    for number in group_numbers:
        client.messages.create(
            to=number,
            from_='+18449932177',
            body=message
        )

sendGroupMessage(group_numbers, message_to_send)
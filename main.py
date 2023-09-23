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
    '+14088271511',
    '+14084982819',
    '+13232828574',
]

#message to send
message_to_send="Hello, I am writing code for Maria. She needs a text message system set up. If you get a text from me Let me know! -Manuel"


def sendGroupMessage(group_numbers, message):
    for number in group_numbers:
        client.messages.create(
            to=number,
            from_='+18449932177',
            body=message
        )
try:
    sendGroupMessage(group_numbers, message_to_send)
except Exception as e:
    print(f"An error occured: {str(e)}")
import os
from twilio.rest import Client

account_sid=os.getenv("ACCOUNT_SID")
token=os.getenv("TOKEN")
my_cell=os.getenv("MY_CELL")
my_twiliocell=os.getenv("MY_TWILIOCELL")


def sendSMS(msg):
  try:
    client=  Client(account_sid, token)
    client.messages.create(to= my_cell , from_= my_twiliocell , body=msg)
    print("SMS sent")
  except:
    print("SMS didn't sent")


sms_text="Hi there, I'm sending this e-mail from Python in Repl.it with environment variables"
sendSMS(sms_text)



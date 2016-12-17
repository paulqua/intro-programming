from twilio.rest import TwilioRestClient

account_sid = "AC59053d0f7c8380079583b6a218c57054" # Your Account SID from www.twilio.com/console
auth_token  = "a544ae2784d07754b7890e59ce1fe0d4"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Who dis be? Nigga!",
    to="+19312474696",    # Replace with your phone number
    from_="+19318003069") # Replace with your Twilio number

print(message.sid)
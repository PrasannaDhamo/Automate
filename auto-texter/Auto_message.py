from twilio.rest import Client 
 
account_sid = 'AC72afce24613e859e132e13957f167501' 
auth_token = input("Enter auth_token : ")
client = Client(account_sid, auth_token) 
 
def love_message():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='message',      
                              to='whatsapp:+919876543210' 
                          )
    print(message.sid)

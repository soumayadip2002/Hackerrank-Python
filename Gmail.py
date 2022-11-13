import smtplib
from email.message import EmailMessage

#Create an Object that will hold all email message details

message = EmailMessage()

EmailContent = 'Email test from Python'
SenderDetails = 'soumayadipsaha2002@gmail.com'
ReceiverDetails = 'soumyadipsaha8327@gmail.com'
#ignorecrowdweb@gmail.com

message['Subject'] = EmailContent
message['From'] = SenderDetails
message['To'] = ReceiverDetails

message.set_content('Hello from python')

EmailSmtp = 'smtp.gmail.com'
server = smtplib.SMTP(EmailSmtp, '587')
server.ehlo()
server.starttls()

emailpass = 'Soumya@2001'
server.login(SenderDetails, emailpass)
server.send_message(message)
server.quit()

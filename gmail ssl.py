import os
import smtplib
from email.message import EmailMessage
import imghdr  # used to determin attachement file type

emailAddress = os.environ.get('GMAIL_ADDR')
emailPass = os.environ.get('GMAIL_APP_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check out this animal'
msg['To'] = 'dsuida@gmail.com'  # to send to multiple, set to a list of email addresses
msg['From'] = emailAddress
msg.set_content("Attached.  Ain't he cute?")

# To send an attachment, need to open the file and examine it.
with open('racoon.jpg', 'rb') as f:  # open as binary file.  Need to specify full path.
    file_data = f.read()
    file_type = imghdr.what(f.name)  # use imghdr to determine file type
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # us SSL method with correct TCP port
    smtp.login(emailAddress, emailPass)  # log into gmail using creds stored as env var
    smtp.send_message(msg)

print('Email sent')
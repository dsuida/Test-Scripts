import os
import smtplib

emailAddress = os.environ.get('GMAIL_ADDR')
emailPass = os.environ.get('GMAIL_APP_PASS')

emailTo = 'dsuida@gmail.com'  # in this case, same as send address, but may not always be so

# format the message using keyword "To" otherwise it is delivered as a BCC
msg = f'To: {emailTo}\nSubject: Test email\nThis is another test.'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # hello to mail server
    smtp.starttls()  # encrypt email
    smtp.ehlo()  # hello again for secure mail
    smtp.login(emailAddress, emailPass)  # log into gmail using creds stored as env var
    smtp.sendmail(emailAddress, emailTo, msg)

print('Email sent')

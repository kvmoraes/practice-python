from email.message import EmailMessage
import ssl
import smtplib

email_sender = input('Write your email: ')

#Pass the password app from your google account
email_password = input('Write your password: ')

email_receiver = input('Write the name of the email receiver: ')

subject = 'Greetings'
body = 'Hello, ' + email_receiver + '!'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
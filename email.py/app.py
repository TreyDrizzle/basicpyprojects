from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'davistyler.chad@gmail.com'
email_password = 'APP PASSWORD'

email_reciever = 'yadaj67051@moneyzon.com'

subject = "This is a test sent by Python"
body = """
This email was sent using Python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())


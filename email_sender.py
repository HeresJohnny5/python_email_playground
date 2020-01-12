import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = 'recipient_email_address'
email['subject'] = 'Email Subject Line'
email.set_content(html.substitute(name='Nacho'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender_email_address', 'sender_email_password')
    smtp.send_message(email)
    print('All Done!')

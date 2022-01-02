import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Savas'
email['to'] = 'write_here_email@gmail.com'
email['subject'] = 'You won million dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('write_your_email@gmail.com', 'your_password')
    smtp.send_message(email)
    print('All good boys!')



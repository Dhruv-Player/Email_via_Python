import smtplib
import getpass
from email.mime.text import MIMEText

def send_email():

    senders_address = 'kherdhruv@gmail.com'
    password = getpass.getpass()
    subject = '""""Learn.Inspire.Grow""""'
    msg = '''Hello Everyone!
             We are pleased to inform you that, we have started our Machine
             Learning and have started working on the first project, i.e.,
             Automation of Python, and currently working on Sending email

             Thank you very much for the efforts by coding club, under the
             humble guidance of sir Abhishek Gupta

             Regards,
             Dhruv Kher
            '''
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senders_address, password)

    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = senders_address
    msg['To'] = 'kherdhruv@gmail.com'
    recipients = 'kherdhruv@gmail.com'

    server.sendmail(senders_address, recipients, msg.as_string())

send_email()

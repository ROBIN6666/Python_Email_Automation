import smtplib
from email.message import EmailMessage


def send_mail(user, passw, to, subject, content, file_name, data):
    msg = EmailMessage()
    msg['subject'] = subject
    msg['from'] = user
    msg['To'] = ", ".join(to)
    msg.set_content(content)

    msg.add_attachment(data, maintype='application', subtype='octet-stream', filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user, passw)
        smtp.send_message(msg)

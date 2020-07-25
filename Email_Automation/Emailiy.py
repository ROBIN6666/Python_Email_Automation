
import os
import smtplib
from email.message import EmailMessage
import imghdr

contact=['rahulkumark72@gmail.com', 'kumarpratyush456@gmail.com']

Email_Address="rahulkumark72@gmail.com"
Email_Password="rahul@234"

msg= EmailMessage()
msg['subject']='Happy birthday'
msg['from']="rahulkumark72@gmail.com"
msg['To']=", ".join(contact)
msg.set_content("file attached...")
 
with open('D:\\Working_logs\\tkkt.pdf', 'rb') as zp:
    file_data = zp.read()
    file_type = imghdr.what(zp.name)
    file_name=zp.name
    # print(file_type)

msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(Email_Address,Email_Password)
    # sub='Happy Birthday'
    # body='When time to celebrate diwali'


    # msg=f'Subject:{sub}\n\n{body}'
    # smtp.sendmail(Email_Address,'rahulkumark72@gmail.com',msg)
    smtp.send_message(msg)

    
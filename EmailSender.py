import smtplib 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import csv
from string import Template

Sender = 'Sender Name'
SenderEmail = 'sender@gmail.com'
SenderPassword = '******'

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

with open('UserInfo.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['last']
        imgfile = row['image']
        fp = open(imgfile, 'rb')
        image = MIMEImage(fp.read())
        fp.close()
        image.add_header('Content-Disposition', "attachment; filename= %s" % row['image'])
        if row['gender'] == 'Male':
            gender = 'Mr.'
        else:
            gender = 'Miss'

        email = MIMEMultipart()
        email['from'] = Sender
        email['to'] = row['email']
        email['subject'] = 'Hi'

        message_template = read_template('MessageTemplate.txt')
        message = MIMEText(message_template.substitute(NAME = name.title(), GENDER = gender))
        email.attach(message)
        email.attach(image)

        with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
            smtp.ehlo()
            smtp.starttls() # encryption method 
            smtp.login(SenderEmail, SenderPassword)
            smtp.send_message(email)
            print('Email sent to ' + row['first'] + ' ' + row['last'])

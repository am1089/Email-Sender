import smtplib 
from email.message import EmailMessage
import csv
from string import Template

ID = 0
FIRST = 1
LAST = 2
GENDER = 3
EMAIL = 4

def get_contacts(filename, UserIds):
    Users = {}
    with open(filename, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Users[row['id']] = [row['first'], row['last'], row['gender'], row['email']]
            UserIds.append(row['id'])
    return Users

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

UserIds = []    
Users = get_contacts('C:Desktop\\PythonCode\\PythonEmail\\UserInfo.csv', UserIds)

for i in range(len(UserIds)):
    id = UserIds[i]
    Info = Users[id]
    name = Info[LAST-1]
    if Info[GENDER-1] == 'Male':
        gender = 'Mr.'
    else:
        gender = 'Miss'

    email = EmailMessage()
    email['from'] = 'Aditya Mitra'
    email['to'] = Info[EMAIL-1]
    email['subject'] = 'Hi'

    message_template = read_template('C:Desktop\\PythonCode\\PythonEmail\\TextFile.txt')
    message = message_template.substitute(NAME = name.title(), GENDER = gender.title())
    email.set_content(message)

    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls() # encryption method 
        smtp.login('adityamitra1089@gmail.com', 'Dj4am69#')
        smtp.send_message(email)
        print('Yes')

#Libraries
from string import Template
import smtplib  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import csv

MY_ADDRESS = 'xx@yy.com'
PASSWORD = 'xxxx'

#Function to read the contacts from a file
def get_contactinfo(filename):
    names=[]
    emails=[]
    namer=0
    mailer=0
    if re.search('\.csv$',filename,flags=re.IGNORECASE) or re.search('\.xlsx$',filename,flags=re.IGNORECASE):
        with open(filename, mode = 'r', encoding='utf-8') as file_contact:
            reader=csv.reader(file_contact)
            headerread = next(reader)
            for i in range(len(headerread)):
                if headerread[i].lower() == 'name':
                    namer = i
                if headerread[i].lower == 'email' or 'email-id':
                    mailer=i
            for a_contact in reader:
                names.append(a_contact[namer])
                emails.append(a_contact[mailer])
        return names, emails
    else:
        with open(filename, mode = 'r', encoding='utf-8') as file_contact:
            for a_contact in file_contact:
                names.append(a_contact.split()[0])
                emails.append(a_contact.split()[1])
        return names, emails        
#returns list with names and emails

def read_template(filename):
    with open(filename, 'r', encoding = 'utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    #read contacts
    names, emails = get_contactinfo('F://EmailPython//mycontacts.csv') 
    message_template = read_template('F://EmailPython//message.txt')
    #Set up SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_ADDRESS, PASSWORD)

    # This part sends the mail to each contact
    for name, email in zip(names, emails):
        msg = MIMEMultipart() #Used to create a message
        # Add in the actual person name to the message template
        message=message_template.substitute(PERSON_NAME=name.title())

        #set up the parameters of the message
        msg['From']= MY_ADDRESS
        msg['To']= email
        msg['Subject'] = 'Do you know I am experimenting?'

        #add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server
        server.send_message(msg)
        del msg
    server.quit()

if __name__ == '__main__':
    main()


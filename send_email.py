import smtplib, ssl
from pydoc import plain
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

date_today = datetime.today().strftime('%Y-%m-%d')
time_now = datetime.today().strftime('%Y-%m-%d %H:%M')

def enviar_email(sender_email,receiver_email,password,file_path):

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    #sender_email = '' #insira o e-mail de envio aqui
    #receiver_email = [''] #insira o array de e-mails aqui
    #password = '' #insira seu password aqui

    mail_content = f'''Dados eventos eSocial

    O presente arquivo foi gerado às {time_now}
    '''

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_email)
    message['Subject'] = f"Eventos eSocial - Dia {date_today}"
    message.attach(MIMEText(mail_content,'plain'))

    #attach_file_name = 'Scripts\csv\eventos_esocial.xlsx'
    attach_file = open(file_path,'rb')
    payload = MIMEBase('application','octet-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition','attachment',filename=file_path)
    message.attach(payload)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email,receiver_email,text)
        server.quit()

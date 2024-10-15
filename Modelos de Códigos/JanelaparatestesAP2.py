import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = 'smtp.gmail.com'
port = '587'
login = 'rpds.lic21@uea.edu.br'
senha = '04741529282'

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login, senha)
corpo = 'Olá tudo bem?'
# montando o e-mail

email_msg = MIMEMultipart()
email_msg['from'] = login
email_msg['To'] = login
email_msg['Subject'] = "Meu e-mail enviado por python"
email_msg.attach(MIMEText(corpo, 'plain'))

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
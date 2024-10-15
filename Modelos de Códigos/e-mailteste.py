import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
host = 'smtp.gmail.com'
port = '587'
email = 'poo.cesit@gmail.com'
senha = 'rjnb fhqw plsp afgz'

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(email, senha)
corpo = """"Assunto: Intimação para Comparecimento – Revisão de Guarda de Menor

Prezada Sra. Elcicleide Queiroz Vieira,

Nos termos do processo judicial n.º 0666756-74.2024.4.03.7276,  referente à revisão da guarda de sua filha Mirela Sebastiana Queiroz Gomes, atualmente sob sua guarda e tutela, e em consonância com o pedido de revisão apresentado pelo Sr. Antônio Benedito Gomes Araújo, o juízo desta Vara da Família determina o seu comparecimento à audiência designada para o dia [data da audiência], às 10:00 dez horas da manhã, a ser realizada no Fórum Fórum Judicial de Nova Olinda do Norte, localizado no endereço Av. Getúlio Vargas Nº 418, na cidade de Nova Olinda do Norte.

A presente audiência visa à análise das condições e circunstâncias atuais, com o objetivo de verificar a necessidade de eventual alteração nas disposições relativas à guarda e convivência da menor. A sua presença é fundamental para garantir o amplo debate das questões que envolvem o bem-estar da criança e para que ambas as partes possam expor suas alegações e fornecer provas pertinentes.

O não comparecimento poderá acarretar prejuízos à sua defesa e ao andamento do processo, além das consequências previstas na legislação vigente.

Solicitamos que, caso tenha advogado constituído, este seja informado para que compareça na data e horário mencionados. Caso não tenha advogado, será possível solicitar a assistência da Defensoria Pública.

Atenciosamente, Fórum Judicial de Nova Olinda do Norte.

"""
# montando o e-mail

email_msg = MIMEMultipart()
email_msg['from'] = email
email_msg['To'] = 'rafaelapeixoto830@gmail.com'
email_msg['Subject'] = "Teste"
email_msg.attach(MIMEText(corpo, 'plain'))

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
print("E-mail enviado!")
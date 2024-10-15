import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = "587"

FROM_EMAIL = "comarcadeNovaOlindadoNorte@hotmail.com"
TO_EMAIL = "rkazuto2@gmail.com"

PASSWORD = getpass.getpass("12345678ryan")
MESSAGE = "teste"

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"{smtp} Echoing code status:{status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.qui()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib, getpass
def sendmail(asunto, sender, reciver, password, mensaje):
	message = MIMEMultipart()
	message["Subject"] = asunto
	message["From"] = sender
	message["To"] = reciver
	message.attach(MIMEText(mensaje, 'plain'))
	server = smtplib.SMTP('smtp.office365.com', 587)
	server.starttls()
	server.login(message["From"], password)
	server.sendmail( message['From'], message['To'], message.as_string())
	server.quit()

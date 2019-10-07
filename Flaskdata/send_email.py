from email.mime.text import MIMEtext
import smtplib

def send_email(email, height):
	from_email="afroscholarproject@gmail.com"
	from_password=  "sweetJesus4life"
	to_email = email


	subject = "Height Data"
	message = "Hey there, your height is %s," %s height
	msg= MIMEText(message, 'html')
	msg['subject'] = to_email
	msg['from'] = from_email


	gmail = smtplib.SMPT('smtp.gmail.com', 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)


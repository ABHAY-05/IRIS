import smtplib
from email.message import EmailMessage

def sendEmail(receiver, subject, message):
	with open('files\\email\\my_email.txt','r') as a:
		b=a.read().split(',')
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(b[0],b[1])
	email = EmailMessage()
	email['From'] = b[0]
	email['To'] = receiver
	email['Subject'] = subject
	email.set_content(message)
	server.send_message(email)

def email_list(name):
	with open('files\\email\\email_list.txt', 'r') as i:
		a=i.read()
		d=dict(x.split() for x in a.splitlines())
	return d[name]

def email_info(command, speak, take_command, my_name):
	if 'send an email to' in command:
		command=command.replace('send an email to','').replace('iris','').replace(' ', '').strip()
		receiver=email_list(command)
		print(f"Receiver's mail: {receiver}")
		speak('What is the subject of your email?')
		subject = take_command()
		speak('Tell me the text in your email')
		message = take_command()
		sendEmail(receiver, subject, message)
		speak(f'done {my_name()}!. Your email is sent')
		speak('Do you want to send more emails?')
		send_more = take_command()
		if 'yes' in send_more:
			email_info(send_more)
		else:
			speak(f'okay {my_name()}')

	else:
		speak('To Whom you want to send email')
		name = take_command()
		receiver=email_list(name)
		print(f"Receiver's mail: {receiver}")
		speak('What is the subject of your email?')
		subject = take_command()
		speak('Tell me the text in your email')
		message = take_command()
		sendEmail(receiver, subject, message)
		speak(f'done {my_name()}!. Your email is sent')
		speak('Do you want to send more emails?')
		send_more = take_command()
		if 'yes' in send_more:
			email_info(send_more)
		else:
			speak(f'okay {my_name()}')
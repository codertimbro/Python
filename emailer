 Emailer for Python 3.7
 #imported Python Packages 
 from email import encoders
 from email.mime.base import MIMEBase 
 from email.mime.text import MIMEText
 from email.mime.multipart import MIMEMultipart
 import smtplib
 
 email_sender = ''     #email address of the sender
 email_receiver = ''   #email address of the recieptant
 subject = ''          #title of the email 
 msg = MIMEMultipart()
 msg['From'] = email_sender
 msg['To'] = email_receiver
 msg['Subject']= subject
 body = ''                                #body of the email information goes here
 msg.attach(MIMEText(body, 'plain'))
 filename = ('')                           #This should be the Attachment path  
 attachment = open(filename,'rb')           
 part = MIMEBase('application', 'octet_stream')
 part.set_payload((attachment).read())
 encoders.encode_base64(part)
 part.add_header('Content-Disposition', "attachment; filename= "+filename)
 msg.attach(part)
 text = msg.as_string()
 connection = smtplib.SMTP('smtp.gmail.com', 587)           #Mail server smtp server information
 connection.starttls()
 connection.login(email_sender, '')                         #Email password 
 connection.sendmail(email_sender, email_receiver, text )
 connection.quit()

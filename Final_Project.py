import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass
fromaddr = str(input("From Email : "))
password = getpass()

f = open("receiver_list.txt", "r")
toaddr = "{}". format (f.read())

msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Final Project"
 
body = "Selamat Hari Raya Idul Fitri. Mohon Maaf Lahir dan Bathin"
 
msg.attach(MIMEText(body, 'plain'))

filename = "idul fitri.jpeg"
attachment = open("D:\Kerja\BPPT\Kerja CPNS\Training AI\Basic Python\\idul fitri.jpeg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


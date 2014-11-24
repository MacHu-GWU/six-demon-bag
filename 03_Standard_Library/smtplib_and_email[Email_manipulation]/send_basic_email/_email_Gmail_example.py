##coding=utf8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

''' step1, basic infomation '''
smtpServer = 'smtp.gmail.com'
fromaddr = 'fromaddr@gmail.com'
toaddr = 'toaddr@gmail.com'
user = 'account' ## account
pw = 'password' ## password
msg = 'welcome to python' ## content

''' step2, create email instance '''
msg = MIMEMultipart() ## create a MIMEMultipart instance
msg['Subject'] = 'This is a test email' ## add subject
att1 = MIMEText(open('test.rar', 'rb').read(), 'base64', 'gb2312') ## set attachment
att1["Content-Type"] = 'application/octet-stream' ## 
att1["Content-Disposition"] = 'attachment; filename="test123.rar"' ## send file as filename
msg.attach(att1) ## attach attachmen

''' step3, create connection to the server, and send email '''
server = smtplib.SMTP() ## create a smtp server
server.connect(smtpServer,587) ## connect to smtpServer, 587 = mandatory authentication
server.ehlo() ## say hi to smtpServer
server.starttls() ## say hi to smtpServer
server.login(user,pw) ## sign in, acc, pw
server.sendmail(fromaddr, toaddr, msg.as_string()) ## send email
print 'sending email'
server.close()



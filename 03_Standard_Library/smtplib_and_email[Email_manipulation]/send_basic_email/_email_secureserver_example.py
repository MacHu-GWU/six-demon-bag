##coding=utf8
import smtplib
from email.mime.text import MIMEText

''' step1, basic infomation '''
smtpServer = 'smtpout.secureserver.net' ## EFA server
fromaddr = 'fromaddr'
toaddr = 'toaddr'

user = 'account' ## account
pw = 'password' ## password
msg = 'welcome to python' ## content

''' step2, create email instance '''
em = MIMEText(msg)
em['Subject'] = 'This is a test email'
em['From'] = fromaddr
em['To'] = toaddr

''' step3, create connection to the server, and send email '''
server = smtplib.SMTP() ## create a smtp server
server.connect(smtpServer,3535) ## connect to smtpServer, gmail use 587
# server.ehlo() ## say hi to smtpServer
# server.starttls() ## Put the SMTP connection in TLS
server.login(user,pw) ## sign in, acc, pw
server.sendmail(fromaddr, toaddr, em.as_string()) ## send email
print 'sending email'
server.close()



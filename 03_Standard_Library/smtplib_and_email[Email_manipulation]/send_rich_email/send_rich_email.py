## coding=utf8
# 邮件的主题包括以下几个部分：
### 必选项 ###
# From: 
# To: 可以是多个收件人
### 可选项 ###
# Subject:
# Content:
# Attachment: 可以是多个附件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def gmail_send(from_addr, to_addr, subject, content, att_box):
    def attachments_sticker(fname_list, msg): ## mutiple attachments attacher.
        for fname in fname_list:
            att = MIMEText(open(fname, 'rb').read(), 'base64', 'gb2312')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="' + fname + '"'
            msg.attach(att)
        return msg
    cnt = MIMEText(content)
    msg = MIMEMultipart() ## create a MIMEMultipart instance
    ''' 发件人 = from_addr '''
    msg['From'] = from_addr
    ''' 收件人 = 一个人，或者多个人 '''
    if type(to_addr) == list: # if list, join together
        msg['To'] = ', '.join(to_addr)
    else: # if not list, to_addr alone
        msg['To'] = to_addr
    ''' 邮件标题 = subject '''
    msg['Subject'] = subject ## add subject
    ''' 邮件正文 = cnt = MINEText(content) '''
    msg.attach(cnt)
    ''' 处理一个或者多个附件 '''
    msg = attachments_sticker (att_box, msg)
    ''' 的'''
    ## < qibaishang is an alias email>
    SMTPserver = 'smtp.gmail.com' ## @@ gmail SMTP server
    user = 'account@gmail.com' ## @@ account
    pw = 'password' ## @@ password
    server = smtplib.SMTP()
    server.connect(SMTPserver,587)
    server.ehlo()
    server.starttls()
    server.login(user,pw)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.close()

from_addr = 'from_addr@gmail.com' ## From address
to_addr = ['to_addr1@gmail.com', 'to_addr2@gmail.com'] ## To address
subject = 'This is a test email'
content = 'welcome to python' ## content
att_box = ['test.txt', 'test.rar']
print 'Sending email...'
gmail_send(from_addr, to_addr, subject, content, att_box) ## send email!
print 'Complete!'



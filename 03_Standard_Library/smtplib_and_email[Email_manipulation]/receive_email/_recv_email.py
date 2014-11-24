##coding=utf-8
import poplib
import email
from email import parser
import chardet

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('username@gmail.com') ## account
pop_conn.pass_('password') ## password

messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
messages = ["\n".join(mssg[1]) for mssg in messages]

counter = 0
for msg in messages:
    counter += 1
    print counter
    msg_ob = parser.Parser().parsestr(msg) ## msg_ob is a email.message.Message
    print 'To = %s' % msg_ob['To'] ## 收件人
    print 'From = %s' % msg_ob['From'] ## 发件人
    print 'Subject = %s' % msg_ob['Subject'] ## 主题
    if msg_ob.is_multipart():
        print '[is_multipart == TRUE]'
        for payload in msg_ob.get_payload():
            print 'get_charset() = %s' % payload.get_charset() ## 无用
            print 'content = %s' % payload.get_payload(decode='utf8') ## 正文 utf8解码
    else:
        print msg_ob.get_payload()
        
#     for property, value in vars(msg_ob).iteritems(): ## 用于打印所有属性名和值
#         print property, ": ", value

''' 结束 '''
# pop_conn.quit() ## 只要执行了这个，相当于数据库的commit。测试时最好不要加
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_poster = {}
mail_poster['163'] = {}
mail_poster['163']['host'] = "smtp.163.com"
mail_poster['163']['user'] = "pedestal_peter"
mail_poster['163']['pass'] = "pedestaldlut"
mail_poster['163']['postfix'] = "163.com"
mail_poster['qq'] = {}
mail_poster['qq']['host'] = "smtp.qq.com"
mail_poster['qq']['user'] = "pedestal_scott"
mail_poster['qq']['pass'] = "pedestaldlut"
mail_poster['qq']['postfix'] = "qq.com"

def send_mail(to_email, sub, context):
    #if re.findall(re_email, to_email)[0][1] == 'qq':
    #    poster = 'qq'
    #else:
    #    poster = '163'
    poster = '163'

    me = mail_poster[poster]['user'] + "<" + mail_poster[poster]['user'] + "@" + mail_poster[poster]['postfix'] + ">"
    msg = MIMEText(context, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_email
    #print msg
    print mail_poster[poster]
    #try:
    send_smtp = smtplib.SMTP()
    send_smtp.connect(mail_poster[poster]['host'])
    send_smtp.login(mail_poster[poster]['user'], mail_poster[poster]['pass'])
    send_smtp.sendmail(me, to_email, msg.as_string())
    send_smtp.close()
    return True
    #except (Exception, e):
    #    print(str(e))
    #    return False

if __name__ == '__main__':
    to_email = raw_input('Input email:')
    sub = raw_input('Input sub:')
    context = raw_input('Input context:')

    print to_email
    print sub
    print context
    send_mail(to_email, sub, context)

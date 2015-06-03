#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
import os
import mimetypes
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pickle
from DSSE_enc import enc
import rsa


def send_mail(to_email, sub, content):
    with open('mail_poster.pickle', 'r') as input:
        mail_poster = pickle.load(input)


    # me = mail_poster['user'] + "<" + mail_poster['user'] + "@" + mail_poster['postfix'] + ">"
    me = mail_poster['user'] + '@' + mail_poster['postfix']
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_email

    pub_path = os.path.join(to_email, 'public.pem')
    with open(pub_path) as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)

    with open('email_tmp', 'wb') as output:
        enc_content = enc(content, pubkey)
        output.write(enc_content)

    ctype, encoding = mimetypes.guess_type('email_tmp')
    if ctype is None or encoding is not None:
        ctype = 'image/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    attachment = MIMEImage((lambda f: (f.read(), f.close()))(open('email_tmp', 'rb'))[0], _subtype = subtype)
    attachment.add_header('Content-Disposition', 'attachment', filename = 'email.enc')
    msg.attach(attachment)

    #try:
    send_smtp = smtplib.SMTP()
    send_smtp.connect(mail_poster['host'])
    send_smtp.login(mail_poster['user'], mail_poster['password'])
    send_smtp.sendmail(me, to_email, msg.as_string())
    send_smtp.close()
    return True
    #except (Exception, e):
    #    print(str(e))
    #    return False

if __name__ == '__main__':
    to_email = raw_input('Input email:')
    sub = raw_input('Input sub:')
    content = raw_input('Input content:')

    print to_email
    print sub
    print content
    send_mail(to_email, sub, content)

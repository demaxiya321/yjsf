#!/usr/bin/env python
#-*- coding: utf-8 -*-

import poplib
from email import parser

host = 'pop3.163.com'
username = 'blessed_alan@163.com'
password = 'demaxiya321...'

pop_conn = poplib.POP3(host)
pop_conn.user(username)
pop_conn.pass_(password)

messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

messages = ['\n'.join(mssg[1]) for mssg in messages]

messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    print 'Subject: ', message['Subject']
pop_conn.quit()

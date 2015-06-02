#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, string
import poplib

host = 'pop3.163.com'
username = 'blessed_alan@163.com'
password = 'demaxiya321...'

pp = poplib.POP3(host)
pp.set_debuglevel(1)
pp.user(username)
pp.pass_(password)
ret = pp.stat()
print ret
tlen = ret[0]

for i in range(1, ret[0]+1):
    mlist = pp.top(i, 0)
    print 'line: ', len(mlist[1])

ret = pp.list()
print ret
down = pp.retr(tlen)
print 'lines: ', len(down)
for line in down[1]:
    print 'line----', line

pp.quit()

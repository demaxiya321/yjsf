#-*- coding: utf-8 -*-
import poplib
import cStringIO, StringIO
import rfc822
import email
import base64
import string

host = 'pop3.163.com'
username = 'blessed_alan@163.com'
password = 'demaxiya321...'

pop = poplib.POP3(host)
pop.set_debuglevel(1)
pop.user(username)
pop.pass_(password)

numMessages = len(pop.list()[1])
print 'num of numMessages', numMessages

hdr, text, octet = pop.retr(numMessages)

buf = cStringIO.StringIO()
for j in text:
	print >>buf, j
buf.seek(0)

text = string.join(text, '\n')
file = StringIO.StringIO(text)

message = rfc822.Message(file)


for k, v in message.items():
	if k == 'from':
		print 'From: ', v
	else:
		pass

msg = email.message_from_file(buf)
for part in msg.walk():
	contenttype = part.get_content_type()
	filename = part.get_filename()

	print 'contenttype: ', contenttype
	print 'filename: ', filename
	if filename and contenttype=='image/octet-stream':
		f = open('mail%d.%s.attach' % (1, filename), 'wb')
		f.write(base64.decodestring(part.get_payload()))
		f.close()
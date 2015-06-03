#-*- coding: utf-8 -*-
import poplib
import cStringIO, StringIO
import rfc822
import email
import base64
import string
import pickle
from DSSE_dec import dec
import os
import rsa

host = 'pop3.163.com'
username = 'blessed_alan@163.com'
password = 'demaxiya321...'

def is_email_from(from_email, message):
	for k, v in message.items():
		if k == 'from':
			print 'from: ', v
			if v == from_email:
				return True
			else:
				return False
		else:
			pass

if __name__ == '__main__':
	from_email = raw_input('Input from email:')
	with open('mail_settings.pickle', 'r') as input:
		mail_settings = pickle.load(input)


	pop = poplib.POP3(mail_settings['host'])
	pop.set_debuglevel(1)
	pop.user(mail_settings['user'])
	pop.pass_(mail_settings['password'])

	private_path = os.path.join(mail_settings['user'], 'private.pem')
	with open(private_path) as privatefile:
		p = privatefile.read()
		privkey = rsa.PrivateKey.load_pkcs1(p)

	numMessages = len(pop.list()[1])
	print 'num of numMessages', numMessages

	for i in range(1, numMessages+1):
		print 'i: ', i
		hdr, text, octet = pop.retr(numMessages)

		buf = cStringIO.StringIO()
		for j in text:
			print >>buf, j
		buf.seek(0)

		text = string.join(text, '\n')
		file = StringIO.StringIO(text)

		message = rfc822.Message(file)


		if is_email_from(from_email, message):
			msg = email.message_from_file(buf)
			for part in msg.walk():
				contenttype = part.get_content_type()
				filename = part.get_filename()

				print 'contenttype: ', contenttype
				print 'filename: ', filename
				if filename and contenttype=='image/octet-stream':
					f = open('mail%d.%s.attach' % (1, filename), 'wb')
					enc_content = base64.decodestring(part.get_payload())
					content = dec(enc_content, privkey)
					print 'content: ', content
					f.write(content)
					f.close()
			break
		else:
			pass
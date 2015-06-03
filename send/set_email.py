#!/usr/bin/env python

import pickle
import getpass
try:
	with open('mail_poster.pickle', 'r') as input:
		mail_poster = pickle.load(input)
except:
	mail_poster = {}
	print 'None Pickle File'

print 'mail_poster: ', mail_poster
mail_poster['host'] = raw_input('Input host:')
mail_poster['postfix'] = raw_input('Input postfix:')
mail_poster['user'] = raw_input('Input user:')
mail_poster['password'] = getpass.getpass('Input password:')

with open('mail_poster.pickle', 'wb') as output:
	pickle.dump(mail_poster, output)
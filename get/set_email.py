#!/usr/bin/env python

import pickle
import getpass
try:
	with open('mail_settings.pickle', 'r') as input:
		mail_settings = pickle.load(input)
except:
	mail_settings = {}
	print 'None Pickle File'

print 'mail_poster: ', mail_settings
mail_settings['host'] = raw_input('Input host:')
mail_settings['user'] = raw_input('Input user:')
mail_settings['password'] = getpass.getpass('Input password:')

with open('mail_settings.pickle', 'wb') as output:
	pickle.dump(mail_settings, output)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Rightpeter'
import rsa
import sys
import os
import re
import zipfile
import myTools
import traceback

enc_pattern = re.compile(r'.*\.enc$')
dec_pattern = re.compile(r'.*\.dec$')


def dec(crypto, privkey):
    content = ''
    while crypto:
        enc_message = crypto[:256]
        crypto = crypto[256:]

        message = rsa.decrypt(enc_message, privkey)
        content += message

    return content


if __name__ == '__main__':
    with open('email_input.txt.enc') as inputfile:
        crypto = inputfile.read()

    print 'crypto:'
    print crypto
    content = dec(crypto)
    print 'content'
    print content
